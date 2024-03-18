---
title: Manually downloading or evicting iCloud files
tags:
  - iCloud
  - macOS
  - Windows
  - snippets
---
iCloud files are stored as a reference to the original file to save space. This is the case when the settings are set to "Optimize Mac storage". However, unlike other providers, iCloud does not allow users to specify which folders should stay on the device or not.

In iCloud for Windows, there's a "pin" functionality that makes a folder stay in the device.[^iCloudPin]

In Finder for Mac, there's the "Download" or "Remove Download" context menu, but that decision might be overrode if iCloud senses that the device is low on space.

However, manually executing commands of `brctl` will indeed trigger a download or eviction of the files.

```bash
cd /the/folder/you/want/to/target
find . -type f -exec brctl evict {} \;
```
[^rakhesh]

`brctl evict` will remove the files from the device.

`brctl download` will download the files to the device.

Similarly, you can use `fileproviderctl materialize` for downloading and `fileproviderctl evict` for removing, which can be used on third party services that do a similar synchronization, like Google Drive or Box.[^fileproviderctlSO]

[^iCloudPin]: [Apple Support: Keep iCloud Drive files downloaded on your Windows computer](https://support.apple.com/en-ca/guide/icloud-windows/icw8531ad6b7/icloud)
[^rakhesh]: [macOS: Remove iCloud downloaded files from a folder (and sub-folders)](https://rakhesh.com/mac/macos-remove-icloud-downloaded-files-from-a-folder-and-sub-folders/)
[^fileproviderctlSO]: [StackOverflow: "brctl evict" and "brctl download" incompatible with Box?](https://stackoverflow.com/a/77100550/147507)
