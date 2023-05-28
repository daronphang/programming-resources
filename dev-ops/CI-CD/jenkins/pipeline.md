## Pipeline

Jenkins Pipeline is a suite of plugins which supports implementing and integrating CD pipelines into Jenkins.

A CD pipeline is an automated expression of your process for getting software from version control right through to your users/customers. Every change to your software (committed in SCM) goes through a complex process on its way to being released. This process involves building the software in a reliable and repeatable manner.

The definition of a Jenkins Pipeline is written into a text file (jenkinsfile) which in turn can be committed to a project's source code repository. This is the foundation of 'Pipeline-as-code', treating the CD pipeline a part of the application to be versioned and reviewed like any other code. The syntax for defining a Pipeline is either in the web UI or with a jenkinsfile, but the latter is considered as best practice.

Creating a jenkinsfile and committing it to source control provides a number of benefits:

- Automatically creates a Pipeline build process for all branches and pull requests
- Code review/iteration on the Pipeline
- Audit trail for the Pipeline
- Single source of truth for the Pipeline

### Pipeline Syntax

A jenkinsfile can be written using two types of syntax: Declarative and Scripted.

Declarative provides richer syntactical features and is designed to make writing and reading Pipeline code easier.

## Examples

### Declarative

```Jenkinsfile
pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'make'
            }
        }
        stage('Test'){
            steps {
                sh 'make check'
                junit 'reports/**/*.xml'
            }
        }
        stage('Deploy') {
            steps {
                sh 'make publish'
            }
        }
    }
}
```

```Jenkinsfile
pipeline {
    agent none  # no global agent is allocated, each stage directive needs to specify instead
    stages {

        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }

        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/add2vals"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }

        # cleanup
        post {
            always {
                echo 'This will always run'
            }
            success {
                echo 'This will run only if successful'
            }
            failure {
                echo 'This will run only if failed'
            }
            unstable {
                echo 'This will run only if the run was marked as unstable'
            }
            changed {
                echo 'This will run only if the state of the Pipeline has changed'
                echo 'For example, if the Pipeline was previously failing but is now successful'
            }
        }
    }
}
```

```Jenkinsfile
def img
pipeline {
    environment {
        registry = "ashishmj/python-jenkins" //To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.
        registryCredential = 'DOCKERHUB'
        githubCredential = 'GITHUB'
        dockerImage = ''
    }
    agent any
    stages {

        stage('checkout') {
                steps {
                git branch: 'master',
                credentialsId: githubCredential,
                url: 'https://github.com/ashish-mj/Jenkins.git'
                }
        }

        stage ('Test'){
                steps {
                sh "pytest testRoutes.py"
                }
        }

        stage ('Clean Up'){
            steps{
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force' //this will delete all images
                sh returnStatus: true, script: 'docker rm ${JOB_NAME}'
            }
        }

        stage('Build Image') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage('Push To DockerHub') {
            steps {
                script {
                    docker.withRegistry( 'https://registry.hub.docker.com ', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy') {
           steps {
                sh label: '', script: "docker run -d --name ${JOB_NAME} -p 5000:5000 ${img}"
          }
        }

      }
    }
```
