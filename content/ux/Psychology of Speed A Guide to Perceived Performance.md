---
title: "Psychology of Speed: A Guide to Perceived Performance"
tags:
  - ux
  - performance
  - psychology
---
Brief notes from the original article available [here](https://calibreapp.com/blog/perceived-performance).

---

Perceived performance refers to how fast or responsive a website or app feels

One commonly invoked principle in the field of psychology is the [[Weber-Fechner law]], which defines the [[Just Noticeable Difference (JND)]] in response to stimulation.

Research indicates that we can only notice a change of more than 20%.

In the web performance context, this means aiming for improvements well above the 20% threshold. This number doesn’t mean that smaller, cumulative improvements don’t count \[...] We’re also better at detecting small differences in time in shorter, rather than longer intervals. Especially when performing routine, quick tasks, we will be more affected by delays. That points us to **optimising actions people perform most frequently**

Bucketing timeframes by attention span (based on [Steve Souw’s definitions](https://www.stevenseow.com/papers/UI%20Timing%20Cheatsheet.pdf) and [research by Rina A. Doherty and Paul Sorenson](https://www.sciencedirect.com/science/article/pii/S2351978915004370)) proves more useful when assessing performance depending on length of the operation and perceived complexity:

| Attention | Category | Response Time | Description |
| :--- | :--- | :--- | :--- |
| **Attentive** | Instantaneous | below 300ms | Perceived as closed-loop system, where people are in direct control. |
| | Immediate | 300ms–1 sec | Perceived as easy to perform.|
| | Transient | 1–5 sec | Perceived as requiring some simple processing, but people still feel like they are making continuous progress. People are unlikely to disengage from task flow. | 
| | Attention span | 5–10 sec | Perceived as requiring more wait time. People need informative feedback to stay engaged. | 
| **Non-attentive** | Non-attentive | 10 sec–5 min | Perceiving as requiring more complex processing. People are likely to disengage and multi-task. | 
| | Walk-away | above 5 min | Perceived as requiring intensive processing. People won’t stay engaged with the task. | 

## 4 ways to improve perceived performance
### 1. Be smart about communicating status and progress

|Load time|Wait time|Strategy|
|---|---|---|
|below 1s|-|No loader needed|
|1–2s|-|Skeleton screen or localised spinner|
|2–10s|Fixed|Time indicator|
||Open-ended|Progress bar or step indicator|
|above 10 s|Fixed|Percentage indicator or background process indicator|
||Open-ended|Notify people when task is complete|

- **Localise loading spinners:** Spinners are best used when only a small page element will change. Avoid using a spinner when entire pages or screens are loading, as it makes [people focus even more on the wait time](https://uxdesign.cc/stop-using-a-loading-spinner-theres-something-better-d186194f771e).

### 2. Always have something for the reader to do

Visitors are never more aware of how long a page takes to load than when they have nothing to do.
### 3. Avoid sudden page movements

These shifts also destroy any illusion that your site is loading quickly, showing that the page is still very much a work in progress.

Luckily, unexpected movement is something we can test and address, thanks to the Cumulative Layout Shift metric. You can find actionable strategies for avoiding sudden page movements in our [Cumulative Layout Shift guide](https://calibreapp.com/blog/cumulative-layout-shift).

### 4. Prevent intensive processing

Reducing and optimising script resources prevents the signs of intensive processing and reduces the possibility of delays. We can use [Interaction to Next Paint](notion://www.notion.so/blog/interaction-to-next-paint) and [Total Blocking Time](notion://www.notion.so/blog/total-blocking-time) to quantify and track these efforts.

