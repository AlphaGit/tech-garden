---
title: QR Codes for Wifi access
tags:
- tools
- qr codes
- wifi
---

([Source](https://blog.jgc.org/2022/07/guest-wifi-using-qr-code.html))

You can create a QR code that allows someone to join a wifi network of your choosing.

The format of the QR code is:

```
WIFI:S:<SSID>;T:<WEP|WPA|blank>;P:<PASSWORD>;H:<true|false|blank>;;
```

`H` is a setting that indicates if the network is hidden or not.

Can always use a tool like https://www.qr-code-generator.com/, if the programmatic generation is not needed.