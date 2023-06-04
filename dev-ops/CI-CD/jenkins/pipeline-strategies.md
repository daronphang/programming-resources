## Serial Integration of PR (Dual Pipeline)

Can implement **dual Pipeline strategy** if PRs are not queuing up waiting to be integrated. It does not permanently reserve a Jenkins executor or make unnecessary API calls to SCM (Github, Bitbucket, etc). Reviewers must check the build status of the first Pipeline before approving.

### Pipeline 1 (PR)

1. Bitbucket triggers a pipeline build when a PR is opened, reopened, or commit is pushed
2. Run automated tests
3. Sends build result to Bitbucket with SUCCESS or FAILED

### Pipeline 2 (Integration)

1. Bitbucket triggers a pipeline build when PR is approved
2. Prevent new commits and post PR comment
3. Merge PR branch to an integration branch
4. Run automated tests
5. Pushes integration branch to origin and delete PR branch

### Pipeline 3 (Continuous Delivery)

Typically artifacts that are generated during the CI process are throw-away, and those branches should be deleted. Instead, store artifacts that are built from long-lived master or release branch source.

1. Bitbucket triggers a pipeline build after the PR has been merged
2. Create artifacts by building from the latest source on master branch
3. Run automated tests
4. Publish artifacts to Artifactory (JFrog)
