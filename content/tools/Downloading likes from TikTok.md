---
title: Downloading likes from TikTok
tags:
  - tools
  - command_line
  - media
date created: 2024-08-03T14:22:36-04:00
date modified: 2024-08-03T14:30:55-04:00
---

1. Log in into your TikTok account
2. Navigate to Settings > Account > Data
3. Download your data
4. On Request Data, select your Activity (which includes Likes), and TXT format
5. Download your data
6. De-compress the zip file
7. Extract the links from your `Activity/Like List.txt`

```bash
cat ~/Downloads/Tiktok/Activity/Like\ List.txt | grep Link | sed 's/Link:\ //' > list.txt
```

8. Install [yt-dlp](https://github.com/yt-dlp/yt-dlp).
9. If on Mac, unblock it from being executed:

```bash
xattr -d com.apple.quarantine yt-dlp_macos
chmod +x ./yt-dlp_macos
mv yt-dlp_macos ~/.local/bin/yt-dlp
```

10. Download all of those. Use IDs as filenames as descriptions can be invalid for filenames.

```bash
yt-dlp -a list.txt -o '%(id)s.%(ext)s'
```
