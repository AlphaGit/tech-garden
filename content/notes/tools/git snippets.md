---
title: git snippets
tags:
- git
- tools
- command line
- snippets
---

## Amending changes in a commit without modifying the message
```bash
git commit -a --amend --no-edit
```

## Displaying only the files modified in a commit
```bash
git show --pretty="" --name-status <commit-ref>
```

## Browsing the repository on a local web interface
```bash
git instaweb
```

(It requires [[lighttpd]] or other httpd daemon. Props to [Cool git commands](https://github.com/Adetona/cool-git-commands) for this one.)

## Search git history for a specific string
```bash
git log -S '<searchString>'
```

## Bring a file from a specific commit
Useful when you want to try everything with the content of your current state, but you want a file/folder to have contents of a specific commit.

```bash
git checkout -- <file-or-folder-path>
```

## Update submodules to the latest branch they're tracking
```bash
git submodule update --recursive --remote
```
