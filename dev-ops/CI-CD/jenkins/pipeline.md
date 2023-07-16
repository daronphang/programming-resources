## Pipeline

Jenkins Pipeline is a suite of plugins which supports implementing and integrating CD pipelines into Jenkins.

A CD pipeline is an automated expression of your process for getting software from version control right through to your users/customers. Every change to your software (committed in SCM) goes through a complex process on its way to being released. This process involves building the software in a reliable and repeatable manner.

Pipeline provides an extensible set of tools for modeling simple-to-complex delivery pipelines "as code" via the **Pipeline domain-specific language (DSL) syntax**.

The definition of a Jenkins Pipeline is written into a text file (jenkinsfile) which in turn can be committed to a project's source code repository. This is the foundation of 'Pipeline-as-code', treating the CD pipeline a part of the application to be versioned and reviewed like any other code. The syntax for defining a Pipeline is either in the web UI or with a jenkinsfile, but the latter is considered as best practice.
