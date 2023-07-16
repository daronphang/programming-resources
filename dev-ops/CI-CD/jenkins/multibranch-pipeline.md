## Multibranch Pipeline

A normal pipeline job is meant for building a single branch from the SCM and deploy to a single environment.

The Multibranch Pipeline project type enables you to implement different Jenkinsfiles for different branches in the source control of the same project. Jenkins automatically discovers, manages and executes Pipelines for branches which contain a Jenkinsfile in source control. Requires you to define where the Jenkinsfile is, and it is **important that the jenkinsfile is in the same location for all the branches you create**.

Multibranch Pipelines can be used for validating pull/change requests with the appropriate plugin i.e. Github, Bitbucket, Gitlab, AWS, etc. This eliminates the need for manual Pipeline creation and management.

A Multibranch job is a folder of Pipeline jobs i.e. for every branch you have, Jenkins will create a folder.

https://devopscube.com/jenkins-multibranch-pipeline-tutorial/

### Branch Exclusion

Can exclude selected branches with Java regex from the UI.

### PR-based Branch Discovery

Builds will get triggered only if a PR is raised. When a developer creates a PR, SCM plugin sends a webhook with the PR information to Jenkins, which will then create a branch Pipeline automatically. SCM will block PRs until a build status from Jenkins is returned.

## Example

```jenkinsfile
pipeline {

    agent {
        node {
            label 'master'
        }
    }

    options {
        buildDiscarder logRotator(
                    daysToKeepStr: '16',
                    numToKeepStr: '10'
            )
    }

    stages {

        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

        stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/spring-projects/spring-petclinic.git']]
                ])
            }
        }

        stage(' Unit Testing') {
            steps {
                sh """
                echo "Running Unit Tests"
                """
            }
        }

        stage('Code Analysis') {
            steps {
                sh """
                echo "Running Code Analysis"
                """
            }
        }

        stage('Build Deploy Code') {
            when {
                branch 'develop'
            }
            steps {
                sh """
                echo "Building Artifact"
                """

                sh """
                echo "Deploying Code"
                """
            }
        }

    }
}
```
