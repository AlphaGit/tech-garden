---
tags:
  - git
  - command_line
  - tools
title: Reducing git history size
---
This is an approach that can be use to safely remove chunky git history, when it becomes troublesome for the developers. However, it requires coordination from the whole team consuming this git repository.

## 1. Cleaning up current state

To make sure there are no un-synced changes before rewriting history:

- Delete any unused branches in the shared version of the repository (if there is one)
- Have everyone commit their uncommitted work and push the changes

At this point, the central repository contains a central authoritarian copy, which is a good place to make changes and have everyone sync on them later on.

## 2. Make the historical deletions on the repository

Deleting the repository history will make it lighter, but the whole set of commits after the offending introductions need to be rewritten.

### 2.1. Analyze what to delete

[`git-filter-repo`](https://github.com/newren/git-filter-repo) is an amazing tool that can check the storage used by already deleted files and folders. 

```bash
git-filter-repo --analyze
code .git/filter-repo/analysis
# see deleted directories
```

## 2.2. Execute filter

At this point, you can issue a command to actually modify the repository. But for safety measures, `git-filter-repo` will unlink the remote repositories. What we'll do is re-add it and push all the branches. Remember that this is risky. However, if it all goes sideways, you always have collaborators' copies as backup (they can always force-push all branches), or you can have a pre-done other clone of the repository.

`--path` filters the repository down to that path, including it in the filter. However, `--invert-paths` reverts the filter, including everything except what was already included.

```bash
git-filter-repo --path <path1> --path <path2> --invert-paths --force

# re-add remote
git remote add origin <gitAddress>

# push branches again
for branch in $(git branch -r | grep -v HEAD); do git push -fu "$branch:${branch#origin/}"; done

# recreate tags
git tag --sort=-creatordate | tail -n +10 > tags.txt
for each $tag in tags.txt git tag push :refs/tags/$tag
```

## 3. Verify everything is fine

Do not skip this step.

Verify everything is alright, including:

1. The repository has decreased in size (re-clone it)
2. All the files are present (directory diff between backup and current repo)
3. All branches are present
4. All tags are present

## 4. Re-sync with team

For each person that needs a copy of the repository:

- Option 1: re-clone repository. This is the best option since it will give them a fresh version of the repository.
- Option 2: for each branch:
	- `git fetch -fp`
	- `git checkout branch`
	- `git reset --hard origin/branch`
