## gitconfig

### Converting HTTP mode to SSH mode

```
[url "ssh://daron.phang@git.byted.org:12345"]
    insteadOf = https://git.byted.org
```

## PAT (Personal Access Token)

Generate PAT and update in git config to cache PAT. After updating git config, git will prompt for username and password (use PAT) for first time operation; subsequent authentications will be cached.

```sh
$ git config --global user.email "daronphang@gmail.com"
$ git config --global credential.helper store
```
