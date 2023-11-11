---
title: iterm2 notifications
tags:
- tools
- automation
- command line
---

We can get different triggers for post notifications when certain events happen in iterm2.

## When a a command finishes
(even if it's chained with other commands):

### Option 1: Manually integrate the notification in the command chain

```bash
myCommand && say "done"
```

### Option 2: Enable alerts

Via `cmd + alt + a`  or via  `Edit > Mark and Annoations > Alerts > Post Notifications`  and this is enough to have iterm2 post a notification to the system notifications engine when the flow of control has changed to another command.

![[iterm2 notifications.png]]
([Source](https://www.stefanjudis.com/today-i-learned/iterm2-offers-a-way-to-notify-you-when-a-long-running-command-has-finished/))

## When new output is detected
For this, iterm2 has a trigger configuration, which can do a lot more than just posting notifications.

For it, go to `Session > Triggers > Add Trigger...`, enter an all-accepting regular expression (`.*`), and set the action to `Post notification`.

![[iterm2 triggers.png]]

([Source](https://apple.stackexchange.com/a/436647/451524))