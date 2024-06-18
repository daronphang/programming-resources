## Overview

Two of the most important questions that people ask themselves after adopting GitOps are:

How should I represent different environments on Git?
How should I handle promoting releases between environments?

## Modeling GitOps environments

Using Git branches for different environments is an **anti-pattern** for the following reasons:

- Using different branches for deployment environments is a relic of the past
- Pull requests and merges between different is problematic
- People are tempted to include environment specific code and create configuration drift
- Branch-per-environment model goes against the existing Kubernetes ecosystem

Instead, you should opt for **environment-per-folder** approach for the following reasons:

- The order of commits on the repo is now irrelevant
- By only copying files around, you only take exactly what you need and nothing else
- You don’t need to use git cherry-picks or any other advanced git method to promote releases
- You are free to take any change from any environment to either an upstream or downstream environment without any constraints about the correct “order” of environments
- You can easily use file diff operations to understand what is different between environments in all directions (both from source and target environments and vice versa)

https://codefresh.io/blog/stop-using-branches-deploying-different-gitops-environments/

https://codefresh.io/blog/how-to-model-your-gitops-environments-and-promote-releases-between-them/

## Promoting between GitOps environments

Scenario: Promote application version from QA to staging environment in the US:

1. copy envs/qa/version.yml envs/staging-us/version.yml
2. Commit/push changes

Scenario: Promote application version from integration testing (GPU) to load testing (GPU) and then to QA:

1. Copy envs/integration-gpu/version.yml envs/load-gpu/version.yml
2. Commit/push changes
3. Copy envs/load-gpu/version.yml envs/qa/version.yml
4. Commit/push changes

Scenario: Promote an application from prod-eu to prod-us along with the extra configuration:

1. Copy envs/prod-eu/version.yml envs/prod-us/version.yml
2. Copy envs/prod-eu/settings.yml envs/prod-us/settings.yml
3. Commit/push changes

In general, all promotions are just **copy operations**. Unlike the environment-per-branch approach, you are now free to promote anything from any environment to any other environment without any fear of taking the wrong changes. Especially when it comes to back-porting configuration, environment-per-folder really shines as you can simply move configuration both “upwards” and “backwards” even between unrelated environments.
