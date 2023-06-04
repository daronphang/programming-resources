## Purpose

To automatically initiate jobs for your Jenkins project with SCM pull request triggers. Can design this capability with a dual pipeline strategy.

The SCM notifier should also be included in the Pipeline so that Jenkins can update SCM with build status.

## Configuration

### Authentication

Best practice is to use Jenkins API token and replace that in the password field.

### SCM Notifier

For Bitbucket, use Stash Notifier.

https://github.com/jenkinsci/stashnotifier-plugin

Alternatively, can use Bitbucket API.

https://developer.atlassian.com/server/bitbucket/how-tos/updating-build-status-for-commits/

## API Testing to Start Build

When testing with API, a CSRF protection token (crumb) is included as an HTTP request header in POST requests to Jenkins as the server uses the "Prevent Cross Site Requests Forgery Exploits" security option.

When a pull request notifier is triggered, it uses a unique Jenkins crumb to start a build job for a Jenkins project with POST. This is done automatically with plugins. However, to test the mechanism, you will need to manually inject with curl.

https://www.jenkins.io/doc/book/security/csrf-protection/

```bash
curl -v -L -u myassistant:JENKINS_API_KEY 'https://jenkins.micron.com/jenkins/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'    # to get crumb
curl -v -L -u myassistant:JENKINS_API_KEY 'https://jenkins.micron.com/jenkins/job/projects/job/p151/job/p151-testing-pipeline/buildWithParameters' -H "Jenkins-Crumb:f26c09..."
```
