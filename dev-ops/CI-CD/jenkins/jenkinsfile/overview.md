## Jenkinsfile

Creating a jenkinsfile and committing it to source control provides a number of benefits:

- Automatically creates a Pipeline build process for all branches and pull requests
- Code review/iteration on the Pipeline
- Audit trail for the Pipeline
- Single source of truth for the Pipeline

### Pipeline Syntax

A jenkinsfile can be written using two types of syntax: Declarative and Scripted.

Declarative provides richer syntactical features and is designed to make writing and reading Pipeline code easier.

## Stages

Assuming everything has executed successfully in the Pipeline, each run will have associated build artifacts archived, test results reported upon and the full console output in Jenkins.

### Build

Stage where source code is assembled, compiled, or packaged. The Jenkinsfile is not a replacement for an existing build tool such as GNU/Make, Maven, Gradle, Bazel, etc, but rather it can be viewed as glue layer to bind the multiple phases of a project's development lifecycle (build, test, deploy) together.

### Test

Running automated tests is a crucial component of any successful continuous delivery process. Jenkins provides a number of plugins for test recording, reporting and visualization i.e. JUnit plugin.

### Deploy

Deployment can imply a variety of steps, depending on the project's requirements i.e. publishing built artifacts to an Artifactory server, pushing code to production system, etc.

You can access the currentBuild.result variable to determine if there were any test failures (unstable).
