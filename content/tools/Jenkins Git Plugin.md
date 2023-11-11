---
title: Jenkins Git Plugin
tags:
- tools
- ci
- jenkins
- git
---

### Refspec

> A refspec maps remote branches to local references. It defines the branches and tags which will be fetched from the remote repository into the agent workspace.
> 
> A refspec defines the remote references that will be retrieved and how they map to local references. If left blank, it will default to the normal `git fetch` behavior and will retrieve all branches. This default behavior is sufficient for most cases.
> 
> The default refspec is `+refs/heads/*:refs/remotes/REPOSITORYNAME/` where REPOSITORYNAME is the value you specify in the above repository "Name" field. The default refspec retrieves all branches. If a checkout only needs one branch, then a more restrictive refspec can reduce the data transfer from the remote repository to the agent workspace. For example, `+refs/heads/master:refs/remotes/origin/master` will retrieve only the master branch and nothing else.
> 
> (...)
> 
> Multiple refspecs can be entered by separating them with a space character. The refspec value `+refs/heads/master:refs/remotes/origin/master +refs/heads/develop:refs/remotes/origin/develop` retrieves the master branch and the develop branch and nothing else.
> 
> Refer to the [git refspec documentation](https://git-scm.com/book/en/v2/Git-Internals-The-Refspec) for more refspec details.

-- [Source](https://plugins.jenkins.io/git/)
