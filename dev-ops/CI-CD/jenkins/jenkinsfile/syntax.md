## Pipeline Syntax

For Declarative Pipeline, the basic statements and expressions follow the same rules as Groovy's syntax with the following exceptions:

- Top-level must be a block i.e. pipeline {}
- No semicolons as statement separators i.e. each statement has to be its own line
- Blocks must only consist of Sections, Directives, Steps, or assignment statements
- A property reference statement is treated as a no-argument method invocation i.e. input as input()

### agent

Must be defined at the top-level inside the pipeline block, but stage-level usage is optional. Allows configuration with parameters i.e. any, none, label, node, docker, kubernetes, etc.

### post

The post section defines one or more additional steps that are run upon the completion of a Pipeline's or stage's run. It can support any of the following post-condition blocks: always, changed, fixed, regression, aborted, failure, success, unstable, unsuccessful and cleanup.

Conventionally, the post section should be placed at the end of the Pipeline.

When declaring agents in individual stages, need to specify node.

```jenkinsfile
post {
    success {
        node(null) {
            script {
                def stash = new myassistant.notifyStash()
                echo 'build succeeded, notifying Bitbucket'
                stash.notifyStash("SUCCESS", "${PULL_REQUEST_FROM_HASH}")
            }
        }

    }
}
```

### triggers

The triggers directive defines the automated ways in which the Pipeline should be re-triggered. For Pipelines integrated with a source such as GitHub or BitBucket, triggers may not be necessary as webhooks-based integration will likely already be present. The triggers available are cron, pollSCM and upstream.

### tools

A section defining tools to auto-install and put on the PATH. This is ignored if agent none is specified.

### when

The when directive allows the Pipeline to determine whether the stage should be executed depending on the given condition, and must contain at least one condition.

### script

script takes a block of Scripted Pipeline and executes in the Declarative Pipeline. For most cases, this step should be unnecessary, but it can provide a useful "escape hatch". Instead, script blocks of non-trivial size/complexity should be moved to **Shared Libraries**.
