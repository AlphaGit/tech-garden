---
title: Building Observability for the 99% developers (DockerCon 2022 notes)
tags:
- conference
- docker
- dockercon
- dockercon2022
- observability
- logs
- security
- sdlc
---

From: https://docker.events.cube365.net/dockercon/2022/content/Videos/925dcd55-d2ee-4059-92c2-ea493bb7bfa9

Problems that this presentation tries to cover:

> "We tried to do testing but we can't really know what happens until we run our system."

or

> "Best practices are very ver hard for us."

This is observability for 99% of developers.

SDLC: Software Development LifeCycle.

Software today is a lot bigger than it used to be. (Code Volume.)

MicroServices are more and more popular. Also, APIs are more and more common.

Testing is falling out of scope because most of what happens is not in the service itself, but rather in the set of services together. So, developers moved from the traditional SDLC into just "maintain, maintain, maintain..."

Debug with debuggers --> We now debug with logs.

Use linters --> Type-checkers don't exist across APIs.

Test before shipping --> where testing in PROD.

This doesn't mean we throw the towel, we just need a different approach.

Observability gap: the reality of observability is that it's hard for people to do logs, traces, and events. It is usually a small part of their jobs, opposed to someone who is dedicated to observability.

99% developers comes from Scott Hanselman, "Dark Matter Developers: The Unseen 99%". Not everyone is Facebook/Google. Best practices for huge companies might not be the same needs/availability that these teams really have.

Possible solutions with low effort:

- eBPF-based passive traffic listening: drop into a system without requiring coe changes. It doesn't fully solve the problem. Also, might be a LOT of data to work with.
- Automatic traffic modelling: use static analysis solutions to create correlations between traffic movements. Suggested product: [[Akita]].
	- It generates suggestions, changes, warnings.

