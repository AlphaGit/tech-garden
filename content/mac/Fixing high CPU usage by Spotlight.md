---
title: Fixing high CPU usage by Spotlight
tags:
  - troubleshooting
  - macos
  - spotlight
  - command_line
---

Sometimes the spotlight process (particularly the `corespotlightd` process), so this is how it can be fixed without a full reinstall ([source](https://developer.apple.com/forums/thread/675482), answer by coinspiranted).

```bash
mdutil -a -i off /
rm -rf ~/Library/Metadata/CoreSpotlight/
sudo rm -rf /System/Volums/Data/.Spotlight-V100
killall -KILL Spotlight spotlightd mds
sudo mdutil -a -i on /
```

As a notice, your terminal application will need to have Full Disk Access (from system preferences) in order to delete those spotlight directories.

