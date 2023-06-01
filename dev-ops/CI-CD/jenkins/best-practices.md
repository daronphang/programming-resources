## Running shell scripts in Jenkins Pipeline

Using a shell script within Jenkins Pipeline can help simplify builds by combining multiple steps into a single stage. The shell script also allows users to add or update commands without having to modify each step or stage separately.

As a general principle, it’s a good idea to keep your Pipeline code (i.e. the Jenkinsfile) as tidy as possible and place more complex build scripting steps into separate shell script files like the test.sh file. This ultimately facilitates the maintenance of your Pipeline, especially if it gains more complexity.
