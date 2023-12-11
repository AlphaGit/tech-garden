---
title: Border Gateway Protocol
tags:
  - networks
  - architecture
  - protocols
---
Border Gateway Protocol (BGP) is the core routing protocol that glues the Internet together and allows [[Autonomous Systems]] (AS) to figure out how to transmit a packet from its source to the destination, potentially traversing multiple intermediate ASes along the way. BGP routing works on a path vector basis - ASes inform their neighbours of the routes they know how to reach, and this information propagates across the Internet.

BGP allows ASes to:

- **Find the best route**
  As data travels across the internet from source to destination, every autonomous system in between has to decide where the data packet should go next.
- **Discover network connection changes**
  The structure of the internet is dynamic. New autonomous systems are being added, and old ones are being removed constantly.
- **Administer network policies**
  BGP has the flexibility to allow autonomous system administrators to implement their own routing policies.
- **Add a layer of network security**
  BGP supports security in your network management.
## Sources

- [Why the Internet Is Both Robust and Fragile](https://blog.bytebytego.com/p/why-the-internet-is-both-robust-and), ByteByteGo NewsLetter
- [What is BGP?](https://aws.amazon.com/what-is/border-gateway-protocol/), AWS Documentation