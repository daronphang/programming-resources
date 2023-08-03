## PAT (Personal Access Token)

Generate PAT and update in git config to cache PAT. After updating git config, git will prompt for username and password (use PAT) for first time operation; subsequent authentications will be cached.

```bash
$ git config --global user.email "daronphang@gmail.com"
$ git config --global credential.helper store
```

## Pushing Files to New Repository

```bash
$ git init <project directory>                #cd /d C:\users\daronphang

$ git branch -m master main
$ git add <--all or example.txt>
$ git status                                  #to see changes committed
$ git commit -a -m "description of changes"
$ git remote add origin <paste GIT URL>
$ git push -u origin master
```

## Revert Commit

```bash
$ git revert <commit id>
$ git add .
$ git commit -m "your changes"
```

## Reset Commit

```bash
$ git reset
$ git reset --hard HEAD # revert back to current head
$ git reset --soft HEAD
```

## Verification

```
$ git log
$ git log src/myassistant/app/api/v1/endpoint.py   # View all changes made to file
```

## Editing Existing Files

```bash
$ git branch                                  # check if branch is master
$ git checkout -b <new branch name>
$ git add <--all or example.txt>
$ git status                                  # to see changes committed
$ git commit -m "description of changes"
$ git push -u origin <new branch name>

$ git remote -v                               # to verify remote repository URL
$ git remote set-url origin <new repo URL>
```

## Misc

```bash
$ cd /d C:\users\daronphang         Cloning repo
$ git clone <repo URL>

$ git checkout master               Switch branch without -b tag
```

## Git Pull

Pull command is used to fetch and download content from remote repository and immediately update local repository to match that content i.e. combination of git.fetch and git.merge. If you don't want to integrate/merge changes directly, use git fetch instead as it will download the new changes only but leaves HEAD branch and working copy files untouched.

To pull other branches from remote repo, use git fetch followed by git pull origin <new_branch_name>.

```bash
$ git pull <remote URL>
$ git pull --no-commit <remote>
$ git pull origin master --allow-unrelated-histories    # When encountered "refusing to merge unrelated histories"

$ git fetch --all # Fetch all branches in remote repo
$ git fetch <remote> <branch>

$ git pull origin <new_branch_name>
$ git pull <repo> <remotebranchname>:<localbranchname>
```

## Viewing/Comparing Changes

```bash
$ git branch -a # check all branches
$ git fetch # update remote repo

$ git diff <local branch> <remote>/<remote branch>
$ git diff main origin/main
$ git diff HEAD
```

```bash
$ git pull origin master
Updating 37b431a..b2615b4
$ git diff 37b431a..b2615b4

$ git reflog | grep -A1 pull | head -2
$ git diff 37b431a..b2615b4
```
