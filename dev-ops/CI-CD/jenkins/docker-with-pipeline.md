## Using Docker with Pipeline

When Pipeline executes, Jenkins will automatically start the specified container and execute the defined steps within it.

```jenkinsfile
pipeline {
    agent {
        docker { image 'node:18.16.0-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
```

### Workspace Synchronization

If you want to keep the workspace synchronized between agents, set reuseNode to true. By default, for containerized stage, Jenkins will:

- Pick any agent
- Create new empty workspace
- Clone pipeline code into it
- Mount this new workspace into the container

When mounting containers, need to cd to WORKDIR specified in Dockerfile, as Jenkins will override this behavior and create a directory with the current Jenkins workspace.
