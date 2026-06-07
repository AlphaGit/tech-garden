---
title: Extract lyrics from beet mp3 files
date created: 2024-08-05T17:27:01-04:00
date modified: 2024-08-05T17:35:59-04:00
tags:
  - tools
  - media
  - snippets
---

(Inspired by [this post](https://discourse.beets.io/t/download-lyrics-as-separate-file/1707/4))

```bat
@echo off
setlocal EnableDelayedExpansion

rem Iterate over each line outputted by `beet ls -p`
for /f "tokens=*" %%f in ('beet ls -p') do (
    set "f=%%f"
    echo "!f!"

    rem Get lyrics using `beet lyrics`
    for /f "delims=" %%L in ('beet lyrics -p "path:!f!" 2^>nul') do (
        set "lyrics=%%L"
    )

    rem Set the name for the .lrc file
    set "lrc=!f:~0,-4!.lrc"

    rem Check if lyrics are found and write to .lrc file
    if defined lyrics (
        echo "-> !lrc!"
        echo "!lyrics!" > "!lrc!"
    ) else (
        echo No lyrics found.
    )
)

endlocal
```
