To further write in detail:

For each person:
- Delete unused branches
- Commit any uncommited work
- Push

```bash
git-filter-repo --analyze
code .git/filter-repo/analysis
# see deleted directories

git-filter-repo --path path1 --path path2 --path path3 --path path4 --invert-paths --force

git remote add origin gitAddress
for branch in $(git branch -r | grep -v HEAD); do git push --force "$branch:${branch#origin/}"; done

git checkout master
git reset --hard origin/master

git push -fu origin master
git push -fu origin branch1
git push -fu origin branch2
git push -fu origin branch3

git tag --sort=-creatordate | tail -n +10 > tags.txt
for each $tag in tags.txt git tag push :refs/tags/$tag
```

For each person:
- Option 1: re-clone repository
- Option 2: for each branch:
	- git fetch -fp
	- git checkout branch
	- git reset --hard origin/branch

#ToProcess 