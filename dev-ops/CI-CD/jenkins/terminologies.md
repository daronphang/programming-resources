### Controller

A central, coordinating process which stores configuration, laods plugins, and renders the various user interfaces for Jenkins.

### Agent

A machine or container which connects to a controller and executes tasks when directed by the controller.

### Build Artifacts

Build artifacts allow you to use the exact same code that was compiled and passed testing. They are files like .exe and .dll that are "attached" to a build in the CI system. Can be downloaded as a zip file and used for deployment.

However, Jenkins is not designed as an artifact repository, and that means:

- Artifacts deployed to a server may be deleted
- No easy way to rollback if artifacts are deleted
- Unclear which Jenkins builds were deployed

The better option is to use a centralized artifact repository like Jfrog or Maven.

### Pipeline

A Pipeline is a user-defined model of a CD pipeline which defines your entire build pr ocess, and typically includes stages for building an application, testing it and delivering it.

### Stage

A stage block defines a conceptually distinct subset of tasks performed through the entire Pipeline, which is used by many plugins to visualize or present Jenkins Pipeline status/progress.

### Step

A single task that tells Jenkins what to do at a particular point in time.

There are powerful steps that 'wraps' other steps i.e. retry, timeout.
