### Use Groovy code in Pipelines as glue

Use Groovy code to connect a set of actions rather than as the main functionality of your Pipeline. In other words, instead of relying on Pipeline functionality (Groovy or Pipeline steps) to drive the build process forward, use single steps (such as sh) to accomplish multiple parts of the build. For instance, using a single Maven build step to drive the build through its build/test/deploy process.

Pipelines, as their complexity increases (the amount of Groovy code, number of steps used, etc.), require more resources (CPU, memory, storage) on the controller. Moreover, for a Pipeline, Groovy code always executes on controller which means using controller resources(memory and CPU). Therefore, it is critically important to reduce the amount of Groovy code executed by Pipelines. Think of Pipeline as a tool to accomplish a build rather than the core of a build.

### Running shell scripts in Jenkins Pipeline

Using a shell script within Jenkins Pipeline can help simplify builds by combining multiple steps into a single stage. The shell script also allows users to add or update commands without having to modify each step or stage separately.

As a general principle, it’s a good idea to keep your Pipeline code (i.e. the Jenkinsfile) as tidy as possible and place more complex build scripting steps into separate shell script files like the test.sh file. This ultimately facilitates the maintenance of your Pipeline, especially if it gains more complexity.
