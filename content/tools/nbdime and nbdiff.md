---
title: nbdime and nbdiff
tags:
- python
- jupyter notebooks
- code review
- tools
---

[nbdime](https://nbdime.readthedocs.io/en/latest/index.html) is a tool that helps with the visual comparison of Jupyter notebooks diffs and merges.

When Jupyter Notebooks are part of git PRs and there is no tool to visualize the diffs, the following steps can be taken to see them visually, locally:

Pre-requisites:

- Follow the [installation instructions](https://nbdime.readthedocs.io/en/latest/installing.html)
	- (For Windows users: remember to add the location where nbdime is installed to your `PATH` variable. The pip install instruction will show a warning with the location of the folder.)
- Follow the [git integration instructions](https://nbdime.readthedocs.io/en/latest/index.html?#git-integration-quickstart)
- For Windows users: you might need to install additional dependencies for nbdiff-web to work. Consider: `pip install jupyter`

To review code:

```bash
git fetch -fp
nbdiff-web origin/master origin/<branch_name_to_review>
```

(You can add `-- <dir>` with the directory path that contains the notebooks to diff.)

You should see a browser window for each notebook that has differences, showing up one at a time. Once you close one, another one will pop up with the next notebook.