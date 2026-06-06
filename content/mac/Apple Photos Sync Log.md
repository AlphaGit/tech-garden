---
title: Apple Photos Sync Log
tags:
  - macOS
  - apple
  - command_line
---
This command line snippet shows the progress of the internals of the iCloud sync log:

```bash
log stream --color always --style compact --predicate '(process == "photolibraryd" or process == "Photos") && (subsystem == "com.apple.photos" or subsystem == "com.apple.photos.cpl")' --level debug
```