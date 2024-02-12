## Bitbucket plugin

### Single pipeline

If using Bitbucket plugin, there is a bug whereby it does not trigger Jenkins build for most Bitbucket events i.e. on PR merge, on push, on PR change. To resolve this, select both options **'on PR merged'** and **'on repo push'**. Alternatively, use 'bitbucket push and pull request' plugin.

### Multi-branch pipeline

Bitbucket plugin works for multi-branch pipeline.
