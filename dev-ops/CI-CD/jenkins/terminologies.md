### Controller

The Jenkins controller is the original node in the Jenkins installation. Administers the Jenkins agents and orchestrates their work, including scheduling jobs on agents and monitoring them. Agents may be connected to the Jenkins controller using either local or cloud computers.

### agent

A machine or container which connects to a controller and executes tasks when directed by the controller. Agents manage the task execution on behalf of the Jenkins controller by using executors.

The agents require a Java installation and a network connection to the Jenkins controller.

Tools required for builds and tests are installed on the node where the agent runs; they can be installed directly or in a container (Docker, Kubernetes, etc).

https://www.jenkins.io/doc/book/using/using-agents/

### nodes

Nodes are the "machines" on which build agents run. In practice, nodes and agents are essentially the same but they are conceptually distinct.

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
