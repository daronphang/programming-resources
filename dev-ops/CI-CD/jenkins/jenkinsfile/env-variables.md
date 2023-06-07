## Using Environment Variables

Jenkins Pipeline exposes env variables via the global variable env, which is available from anywhere within a Jenkinsfile. The variables are documented at ${YOUR_JENKINS_URL}/pipeline-syntax/globals#env.

## Setting Environment Variables (Declarative)

Declarative Pipeline supports an environment directive.

### Static

```jenkinsfile
pipeline {
    agent any
    environment {
        CC = 'clang'
    }
    stages {
        stage('Example') {
            environment {
                DEBUG_FLAGS = '-g'
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
```

### Dynamic

Env variables can be set at runtime using sh, bat or powershell scripts. Each script can either returnStatus or returnStdout.

```jenkinsfile
pipeline {
    agent any
    environment {
        // Using returnStdout
        CC = """${sh(
                returnStdout: true,
                script: 'echo "clang"'
            )}"""
        // Using returnStatus
        EXIT_STATUS = """${sh(
                returnStatus: true,
                script: 'exit 1'
            )}"""
    }
    stages {
        stage('Example') {
            environment {
                DEBUG_FLAGS = '-g'
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
```

### Credentials

Jenkin's declarative Pipeline syntax has the credentials() helper method, used within the environment directive.

## Variables

### BUILD_ID

The current build ID, identical to BUILD_NUMBER for builds created in Jenkins versions 1.597+

### BUILD_NUMBER

The current build number, such as "153"

### BUILD_TAG

String of jenkins-${JOB_NAME}-${BUILD_NUMBER}. Convenient to put into a resource file, a jar file, etc for easier identification

### BUILD_URL

The URL where the results of this build can be found (for example http://buildserver/jenkins/job/MyJobName/17/ )

### EXECUTOR_NUMBER

The unique number that identifies the current executor (among executors of the same machine) performing this build. This is the number you see in the "build executor status", except that the number starts from 0, not 1

### JAVA_HOME

If your job is configured to use a specific JDK, this variable is set to the JAVA_HOME of the specified JDK. When this variable is set, PATH is also updated to include the bin subdirectory of JAVA_HOME

### JENKINS_URL

Full URL of Jenkins, such as https://example.com:port/jenkins/ (NOTE: only available if Jenkins URL set in "System Configuration")

### JOB_NAME

Name of the project of this build, such as "foo" or "foo/bar".

### NODE_NAME

The name of the node the current build is running on. Set to 'master' for the Jenkins controller.

### WORKSPACE

The absolute path of the workspac

## Credentials

When using credentials, select the appropriate kind in Credentials folder. To use them in Pipeline, can wrap them using withCredentials method. Variable defined will be used to access the variable/file in the Pipeline. CredentialsId is the id you have defined in Credentials folder.

```groovy
withCredentials([file(credentialsId: 'EMAIL_SERVICE_ENV', variable: 'EMAIL_SERVICE_ENV')]) {
    sh "cp /${EMAIL_SERVICE_ENV} ${WORKSPACE}/packages/email_service/mmail"
}
```
