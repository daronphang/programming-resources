## String Interpolation

Jenkins Pipeline uses rules identical to Groovy for string interpolation. Supports both single or double quotes, but **double quotes are required for string interpolation**.

Groovy string interpolation can leak sensitive environment variables and **should never be used with credentials**.

```groovy
def username = 'Jenkins'
echo "Hello Mr. ${username}"
```

## Handling Parameters

Declarative Pipeline supports parameters out-of-the-box, allowing the Pipeline to accept user-specified parameters at runtime, via the parameters directive. The parameters are accessible as members of the params variable.

The parameters directive provides a list of parameters that a user should provide when triggering the Pipeline. Each parameter has a Name and Value.

https://www.jenkins.io/doc/book/pipeline/syntax/#parameters

```jenkinsfile
pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')
        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"
                echo "Biography: ${params.BIOGRAPHY}"
                echo "Toggle: ${params.TOGGLE}"
                echo "Choice: ${params.CHOICE}"
                echo "Password: ${params.PASSWORD}"
            }
        }
    }
}
```

## Handling Failure

Declarative Pipeline supports robust failure handling by default via its post section which allows declaring a number of different "post conditions" such as always, unstable, success, failure, and changed.

```jenkinsfile
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'make check'
            }
        }
    }
    post {
        always {
            junit '**/target/*.xml'
        }
        failure {
            mail to: team@example.com, subject: 'The Pipeline failed :('
        }
    }
}
```

## Using Multiple Agents

Can be useful for more advanced use-cases such as executing builds/tests across multiple platforms.

```jenkinsfile
pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                checkout scm
                sh 'make'
                stash includes: '**/target/*.jar', name: 'app'
            }
        }
        stage('Test on Linux') {
            agent {
                label 'linux'
            }
            steps {
                unstash 'app'
                sh 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }
        stage('Test on Windows') {
            agent {
                label 'windows'
            }
            steps {
                unstash 'app'
                bat 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }
    }
}
```

## Parallel Execution

Instead of executing the tests on "linux" and "windows" in series, can execute in parallel.

```jenkinsfile
pipeline {
    stage('Build') {
        /* .. snip .. */
    }

    stage('Test') {
        parallel linux: {
            node('linux') {
                checkout scm
                try {
                    unstash 'app'
                    sh 'make check'
                }
                finally {
                    junit '**/target/*.xml'
                }
            }
        },
        windows: {
            node('windows') {
                /* .. snip .. */
            }
        }
    }
}
```
