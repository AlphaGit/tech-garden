---
title: Troubleshooting iCloud Drive Sync
tags:
  - macOS
  - troubleshooting
  - iCloud
---
```bash
log show | grep Cloud | grep Error
```

Need to troubleshoot errors one by one.

---

> Platform Binary: Could not create code from path /Volumes/Macintosh HD - Data/Library/Developer/CommandLineTools/SDKs/MacOSX12.1.sdk/System/Library/PrivateFrameworks/UARPiCloud.framework

Fixed by re-installing command lines:

```bash
xcode-select --install
```

(And continue in the pop up window. It might pop up in the background, so look out for that.)

---

> fileproviderd: \[com.apple.FileProvider:com.apple.CloudDocs.iCloudDriveFileProvider/0{34}9] ┳377cf68 ‼️  done executing \<J1 ‼️  update-item(propagated:\<fcc50 dbver:3 domver:\<nil>> diffs:hidden|evictable|structure) why:itemChangedRemotely sched:utility#1702559433.895729 error:\<NSError: POSIX 13 "The operation couldn’t be completed. Permission denied" >> →  \<requested:\<p:fileID(29725048) n:"_{6}_.py" doc sz:374 m:rw-%<72220581> ct:1670961965.0 mt:1670961965.0>> \[duration 7ms476µs]

In my case, some of my files being synced did not belong to my own user (I migrated from another user). This can be fixed by:

```bash
cd ~/Library/Mobile\ Documents
sudo chown -R alpha .
```

(Replace `alpha` by your own username.)

---

> itunescloudd: \[com.apple.amp.itunescloudd:Default] \<ICDCloudServiceStatusMonitor: 0x7fc18310af20>: Could not find valid cloud service capabilities; error: Error Domain=ICError Code=-7007 "Privacy acknowledgement required, but presenting the privacy prompt is not allowed." UserInfo={NSDebugDescription=Privacy acknowledgement required, but presenting the privacy prompt is not allowed.}.

Open the AppStore app, log in if not logged in already, select "Create" and accept the terms for app updates. Do the same with the Music and TV apps, make sure you're logged in.

(Could not solve completely.)

---

> itunescloudd: \[com.apple.amp.itunescloudd:Default] \<ICDCloudServiceStatusMonitor: 0x7fc18310af20>: Could not find valid cloud service capabilities; error: Error Domain=ICError Code=-7007 "Privacy acknowledgement required, but presenting the privacy prompt is not allowed." UserInfo={NSDebugDescription=Privacy acknowledgement required, but presenting the privacy prompt is not allowed.}.
> itunescloudd: (iTunesCloud) \[com.apple.amp.iTunesCloud:Subscription] \<ICMusicSubscriptionStatusRequestOperation: 0x7fc18121e410> Returning last known subscription status (null) with error Error Domain=ICError Code=-7008 "(null)" for: \<ICStoreRequestContext: 0x7fc18121e9e0 \[itunescloudd/1.0; \<ICUserIdentity 0x7fc18314a820: \[Active Account: \<signed out>]>]>
> itunescloudd: (iTunesCloud) \[com.apple.amp.iTunesCloud:Subscription] Delivering result for \<ICMusicSubscriptionStatusRequest: 0x7fc183028200; storeRequestContext = \<ICStoreRequestContext: 0x7fc183028770 \[parsecd/1.0; \<ICUserIdentity 0x7fc18314a820: \[Active Account: \<signed out>]>]>; allowsFallbackToExpiredStatus = YES; allowsFallbackToStatusNeedingReload = YES; carrierBundleProvisioningStyle = once; shouldReturnLastKnownStatusOnly = YES; requestIdentifier = B920EFEB-B502-4874-9C62-C01BE46DAAA1> to 1 status handler: error = Error Domain=ICError Code=-7008 "(null)".
> parsecd: (iTunesCloud) \[com.apple.amp.iTunesCloud:Subscription] Delivering result for \<ICMusicSubscriptionStatusRequest: 0x7f7cdc4443b0; storeRequestContext = \<ICStoreRequestContext: 0x7f7cdc4451b0 \[parsecd/1.0; <ICUserIdentity 0x7f7cdc445210: \[Active Account: \<signed out>]>]>; allowsFallbackToExpiredStatus = YES; allowsFallbackToStatusNeedingReload = YES; carrierBundleProvisioningStyle = once; shouldReturnLastKnownStatusOnly = YES; requestIdentifier = B920EFEB-B502-4874-9C62-C01BE46DAAA1> to 1 status handler: error = Error Domain=ICError Code=-7008 "(null)".
> itunescloudd: (iTunesCloud) \[com.apple.amp.iTunesCloud:Subscription] \<ICMusicSubscriptionStatusRequestOperation: 0x7fc181324220> Aborted fetching subscription status because privacy link needs to be displayed first.

Most of the errors seem to be related to no iCloud account being set, although I am logged in to my iCloud account. Navigate to settings, iCloud, and "Sign out..." at the bottom. When asked about keeping a copy or deleting copies, choose whatever suits you best. I said to keep a copy of contacts and passwords, deleted photos, and waited for the system to log me out.

Make sure to restart completely once logged out from iCloud.

Then log in to iCloud, merge all the data and wait forever while it syncs.

Wait until it's all synced (or stuck) before continuing. Otherwise, we might end up troubleshooting false-positives.

---

> itunescloudd: (iTunesCloud) \[com.apple.amp.iTunesCloud:Default] \<ICURLBagProvider: 0x7fc18071c380> Encountered error creating cache directory at /Users/alpha/Library/Application Support/com.apple.iTunesCloud/URLBags/itunescloudd. error=Error Domain=NSCocoaErrorDomain Code=513 "You don’t have permission to save the file “itunescloudd” in the folder “URLBags”." UserInfo={NSFilePath=/Users/alpha/Library/Application Support/com.apple.iTunesCloud/URLBags/itunescloudd, NSUnderlyingError=0x7fc18312e520 {Error Domain=NSPOSIXErrorDomain Code=1 "Operation not permitted"}}

This error seems to be related to "sandboxing" restrictions. ([Source](https://developer.apple.com/forums/thread/96062))

Removed the folder (actually, just moved it as a backup) and rebooted.

```bash
cd ~/Library/Application\ Support
mv com.apple.iTunesCloud com.apple.iTunesCloud.bkp
```

---

At this point the iCloud UI reports that all files have been synced successfully, but the logs keep reporting errors.

It's possible that some of these sync errors are because of GoogleDrive, which also uses `fileproviderd`,  but for which I refuse to give access to all my hard drive.

---

Useful tool to lookup OS Error codes: [[OSStatus]]