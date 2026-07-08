---
title: AI-Coded Applications Risk Catalog
summary: "Catalog of risks in vibecoded/AI-coded applications: security, quality, operational, legal, and human-factor issues with severity, probability, mitigations, and sources"
tags:
  - ai
  - llm
  - security
date created: 2026-07-07T00:00:00-04:00
date modified: 2026-07-08T00:00:00-04:00
---

Catalog of known issues with vibecoded / AI-coded applications, compiled from studies, security research, and documented incidents (researched 2026-07-07).

## Evaluation Criteria

**Severity** — impact if the risk materializes:

- 🔴 **High** — data breach, destroyed production data, legal/regulatory exposure, exploitable security holes (excludes risks whose impact is purely cost)
- 🟡 **Medium** — high cost, degraded quality, recoverable damage
- 🟢 **Low** — slower delivery, small quality issues (non-functionality-breaking)

**Probability** — where measured numbers exist, they are used directly; where they don't, the figure is an estimate (marked *est.*) of how feasible it is that the conditions for the issue are given in a regular company:

- 🔴 **High** — 50%+
- 🟡 **Medium** — 20–49%
- 🟢 **Low** — <20%

Incidence rates, study names, and incident details live in the footnotes.

## 1. Security

### 1.1 Insecure code generation by default

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (45%, measured)
- Models reproduce insecure patterns from their training data and optimize for code that runs, not code that resists attack. A large share of AI-generated code contains exploitable weaknesses out of the box, and newer or larger models have not meaningfully improved this.[^veracode][^csa]
- **Mitigations:**
  - Treat all AI output as untrusted third-party code; mandatory human review before merge
  - SAST/DAST/SCA in CI (Semgrep, CodeQL, Bandit, dependency scanning)
  - Security-focused system prompts / rules files[^openssf]

### 1.2 Broken or missing authentication & authorization

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (40%, measured)
- AI-generated auth logic frequently compiles and "works" while allowing any user to reach other users' data: missing authorization checks, client-side-only auth, and even inverted access-control conditions. Nothing flags the gap because the happy path behaves correctly.[^ibm][^wiz][^vibeappscanner]
- **Mitigations:**
  - Never let AI design the auth model; use battle-tested frameworks/providers (Auth0, Supabase Auth, etc.)
  - Explicit authorization tests per endpoint (positive and negative cases)
  - Penetration test before launch for anything holding user data

### 1.3 Hardcoded secrets and client-side API keys

- **Severity:** 🔴 High · **Probability:** 🟢 Low (15%, measured)
- The AI puts credentials wherever the feature works fastest — often directly in client-side code, where anyone can read them with browser dev tools. Consequences: stolen keys, drained API billing accounts, full database access.[^arnica][^escape][^vibeappscanner]
- **Mitigations:**
  - Secret scanning in CI and pre-commit (gitleaks, trufflehog)
  - Server-side proxy for all third-party API calls; keys only in env vars / secret managers
  - Billing alerts and spend caps on all API accounts

### 1.4 Misconfigured backends (RLS off, open buckets, exposed endpoints)

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (20%, measured)
- AI scaffolding favors convenient-but-insecure defaults: database row-level security disabled, unencrypted storage buckets, open HTTP endpoints, permissive CORS. Whole production databases have been readable by anyone within days of launch.[^wiz][^securityscanner][^csa]
- **Mitigations:**
  - Infrastructure/config review checklist before any public deploy
  - Automated cloud misconfiguration scanning (CSPM)
  - Default-deny database policies; verify RLS/ACLs explicitly

### 1.5 Classic injection flaws (XSS, SQLi, SSRF, log injection)

- **Severity:** 🔴 High · **Probability:** 🔴 High (86%, measured)
- Generated code routinely concatenates untrusted input into queries, HTML, logs, and outbound requests. The decades-old injection classes that frameworks and training were supposed to eliminate come back at scale because the model reproduces vulnerable idioms.[^veracode][^csa]
- **Mitigations:**
  - Parameterized queries and ORM usage enforced by lint rules
  - Output encoding / templating frameworks with auto-escaping
  - SAST rules tuned for injection patterns; DAST on staging

### 1.6 Hallucinated dependencies / slopsquatting

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (20%, measured)
- Models confidently import packages that don't exist. Attackers register those predictable names on public registries with malicious payloads, so the next developer who installs the AI's suggestion executes attacker code — a supply-chain attack more scalable than typosquatting.[^trend][^fossa]
- **Mitigations:**
  - Verify every new dependency exists, is maintained, and has real usage before install
  - Lockfiles + private registry/proxy with allowlists
  - SCA tooling that flags newly published or low-reputation packages

### 1.7 Prompt injection against the coding agent itself

- **Severity:** 🔴 High · **Probability:** 🟢 Low (est. 15%)
- Malicious instructions hidden in content the agent reads — web pages, READMEs, issue text, rules files, MCP tool descriptions — can hijack it into generating backdoored code, exfiltrating secrets, or running arbitrary commands. The attack surface is everything the agent ingests, not just the code.[^hackernews][^arxiv-pi]
- **Mitigations:**
  - Review rules files and MCP server configs like code (they are attack surface)
  - Least-privilege agents: no prod credentials, sandboxed execution, restricted network
  - Human approval gates for shell commands and dependency installs

### 1.8 Security degradation over iterative generation

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (est. 40%)
- Repeatedly asking a model to "improve" or extend its own code progressively degrades security — each iteration compounds subtle flaws rather than fixing them. Long vibe-coding sessions where the model rewrites its own output are the worst case.[^arxiv-deg]
- **Mitigations:**
  - Re-run security scans after every AI iteration, not just the first
  - Prefer small, reviewable diffs over full-file regeneration

### 1.9 Outdated or vulnerable dependency choices

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 60%)
- Trained on old code, models suggest deprecated libraries, end-of-life versions, and APIs with known CVEs. The volume of AI-generated code multiplies the rate at which known-vulnerable dependencies enter codebases.[^csa]
- **Mitigations:**
  - Dependency freshness/vulnerability scanning (Dependabot, Renovate, OWASP Dependency-Check)
  - Pin versions; review AI-suggested dependencies against current advisories

### 1.10 Missing rate limiting, input validation, and abuse controls

- **Severity:** 🔴 High · **Probability:** 🔴 High (est. 60%)
- AI builds the happy path: endpoints with no rate limits, no validation, no abuse protection. This enables scraping, brute force, and denial-of-wallet attacks where attackers burn the owner's metered API budget through wide-open endpoints.[^securityscanner]
- **Mitigations:**
  - API gateway with rate limiting and quota enforcement by default
  - Input validation schemas (zod, pydantic) required at every boundary
  - Cost alerts on all metered services

### 1.11 PII and sensitive data exposure

- **Severity:** 🔴 High · **Probability:** 🟢 Low (10%, measured)
- Personal data leaks through client bundles, unprotected endpoints, verbose error messages, and logs — because the AI returns whatever data shape makes the feature work, including raw database records with fields the user should never see.[^escape][^arnica][^wiz]
- **Mitigations:**
  - Data classification pass before launch: what PII exists, where it flows
  - Never return raw DB objects from APIs; explicit response DTOs
  - Disable verbose errors/stack traces in production

## 2. Code Quality & Maintainability

### 2.1 Technical debt explosion / code duplication

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 80%)
- AI regenerates similar logic instead of reusing existing code, so codebases accumulate near-duplicate blocks at a pace refactoring can't match. Duplication compounds: every bug fix and behavior change must now be applied in several places, and usually isn't.[^gitclear]
- **Mitigations:**
  - Duplication metrics in CI (SonarQube, jscpd) with thresholds
  - Scheduled refactoring budget; treat AI output as a draft to consolidate
  - Prompt the AI with existing modules/utilities as context

### 2.2 High code churn / rework

- **Severity:** 🟢 Low · **Probability:** 🔴 High (est. 70%)
- A growing share of AI-generated lines get reverted or rewritten within weeks of landing. Velocity gains are partly illusory — code ships faster and gets redone faster, and the redo work is invisible in most team metrics.[^gitclear]
- **Mitigations:**
  - Track churn as a first-class metric alongside velocity
  - Smaller PRs with real review, not rubber-stamping

### 2.3 "Almost right" code and subtle logic bugs

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (66%, measured)
- The signature AI failure mode: code that passes superficial inspection but embeds wrong edge-case behavior, off-by-one errors, and misunderstood requirements. Finding and fixing these often costs more than writing the code by hand would have.[^so2025][^modall]
- **Mitigations:**
  - Test-first workflows: write (or at least review) the tests yourself
  - Require the author to explain the generated code in review
  - Property-based and edge-case testing for critical logic

### 2.4 Hallucinated APIs, functions, and configuration

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 50%)
- Beyond packages, models invent methods, parameters, config keys, and framework behaviors that don't exist or belong to other versions. Fails fast when it breaks the build; dangerous when it silently no-ops (e.g. a security setting that isn't real).
- **Mitigations:**
  - Compile/typecheck/lint in a tight loop; strong typing catches much of this
  - Verify unfamiliar APIs against official docs for the pinned version

### 2.5 No automated tests

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 85%)
- AI generates features, not the safety net around them. Without tests, every subsequent prompt can silently break previously working flows — there is no regression signal at all in a codebase that changes as fast as prompts can be typed.[^autonoma][^redwerk]
- **Mitigations:**
  - Make tests part of the definition of done; ask the AI to generate tests and review them critically
  - CI gate on coverage for critical paths (auth, payments, data access)

### 2.6 Architecture erosion / accidental coupling

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 80%)
- The model optimizes locally per prompt with no global design, producing code that looks modular but shares state, tables, and globals under the hood. Middleware and business logic end up scattered with no coherent mental model behind them.[^altersquare][^codecentric]
- **Mitigations:**
  - Human-owned architecture: define boundaries/contracts before generating code
  - Architectural fitness functions and dependency rules in CI
  - Periodic design reviews of AI-grown modules

### 2.7 Unmaintainable codebase → forced rewrite

- **Severity:** 🟡 Medium · **Probability:** 🟡 Medium (est. 30%)
- The compounding endgame of the risks above: nobody holds a mental model of the system, debugging becomes archaeology, and when requirements change the cheapest path is a from-scratch rewrite — typically right when the app has gained real users.[^redwerk][^osmani]
- **Mitigations:**
  - Keep humans in the comprehension loop from day one (review, docs, ADRs)
  - Refactor incrementally before debt compounds; budget for hardening sprints

### 2.8 Missing error handling and edge cases

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 75%)
- Generated code assumes ideal conditions: clean inputs, single user, small datasets. Missing try/catch, unhandled promise rejections, no graceful degradation, no handling of empty or malformed input. Works in the demo, fails with real users.[^modall][^altersquare]
- **Mitigations:**
  - Explicitly prompt for failure modes; review error paths, not just happy paths
  - Chaos/fault-injection testing for critical services

## 3. Operational & Reliability

### 3.1 Scalability and performance failures

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 70%)
- No database indexes on queried columns, N+1 query patterns, no caching, no pagination, no connection pooling. The app works for one demo user and collapses at modest real-world load — and retrofitting performance is far more expensive than designing for it.[^modall][^codeconductor]
- **Mitigations:**
  - Load testing before launch; query analysis (EXPLAIN) on hot paths
  - Indexing and pagination review as a launch checklist item

### 3.2 Destructive autonomous agent actions

- **Severity:** 🔴 High · **Probability:** 🟢 Low (est. 5%)
- An agent with production access can delete databases, overwrite code, or fabricate data in a single autonomous action — including while explicitly instructed not to act — and then misreport what it did or whether recovery is possible.[^fortune][^toms][^aiid]
- **Mitigations:**
  - Agents never get production credentials; hard environment separation
  - Human approval for destructive operations; immutable, tested backups
  - Planning/read-only modes for exploration

### 3.3 No observability, logging, or audit trail

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 80%)
- AI doesn't add logging, metrics, or tracing unless asked. When the app breaks there is nothing to diagnose with; for regulated data, the missing audit trail is itself a compliance violation (see 4.3).[^pinklime]
- **Mitigations:**
  - Observability as an explicit requirement in prompts and review
  - Standard logging/tracing middleware baked into the project template

### 3.4 Fragile builds from unpinned dependencies

- **Severity:** 🟢 Low · **Probability:** 🟡 Medium (est. 40%)
- AI-scaffolded manifests use loose version ranges, so installs pull whatever upstream shipped last night; breaking changes stop the build with no code change. Combined with no tests, the breakage surfaces in production.[^autonoma]
- **Mitigations:**
  - Commit lockfiles; exact pinning for critical deps; Renovate with CI verification

### 3.5 Platform / vendor lock-in

- **Severity:** 🟡 Medium · **Probability:** 🟡 Medium (est. 30%)
- App-builder platforms can hide or own the files, database, auth, and hosting. Export paths are limited; leaving means rebuilding, and a pricing or capability change on the platform's side can strand the product.[^codeabides][^flatlogic]
- **Mitigations:**
  - Prefer tools that operate on a standard repo; keep everything exportable (code, schema, data)
  - Own your domain, DNS, and database from day one

## 4. Legal, Licensing & Compliance

### 4.1 Open-source license contamination

- **Severity:** 🔴 High · **Probability:** 🟢 Low (est. 10%)
- Models trained on copyleft code can reproduce near-verbatim licensed snippets without attribution, silently stripping GPL/AGPL obligations from the output. Provenance of generated code is essentially unauditable, and contamination discovered late can force rewrites.[^dna][^laundering]
- **Mitigations:**
  - Code-similarity / snippet-scanning tools (duplication detection in SCA suites)
  - Duplicate-detection settings in assistants (e.g. Copilot's public-code filter)
  - Treat AI output as third-party contribution in your OSS policy

### 4.2 No copyright protection over AI output

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 60%)
- Purely AI-generated code likely can't be copyrighted (no human authorship) while it can still infringe someone else's copyright — all the liability, none of the protection. Vendors' terms disclaim responsibility for infringement in output. Matters for IP-based valuation, exclusivity, and client contracts.[^paddo][^dna]
- **Mitigations:**
  - Meaningful human authorship/modification over shipped code; document it
  - Contract language allocating AI-related IP risk with clients
  - Legal review of assistant ToS/indemnification (some enterprise tiers indemnify)

### 4.3 Regulatory compliance gaps (GDPR, HIPAA, SOC 2)

- **Severity:** 🔴 High · **Probability:** 🔴 High (est. 50%)
- AI-generated boilerplate omits what regulations require: audit logging of data access, retention and deletion flows, encryption at rest, consent handling, data residency. The AI implements what you specify — and compliance is rarely specified, so teams discover the gap when auditors ask.[^pinklime][^taction]
- **Mitigations:**
  - Compliance requirements written into prompts/rules files for regulated projects
  - Compliance review gate on data flows and infra config before production
  - Data protection impact assessment when personal data is involved

### 4.4 Accountability and liability gap

- **Severity:** 🟡 Medium · **Probability:** 🟡 Medium (est. 30%)
- When AI-written code causes harm, liability lands on whoever shipped it — the vendor disclaims everything, and "the AI wrote it" is not a defense. Professional-negligence exposure for agencies delivering AI-coded work to clients without disclosure or review.[^paddo]
- **Mitigations:**
  - Same review/signoff standards as human code; a named human owns every merge
  - Disclose AI-assisted development where contractually relevant

## 5. Human & Process Factors

### 5.1 Developer skill atrophy and shallow comprehension

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 60%)
- Delegating generation wholesale measurably reduces how well developers understand the code and libraries they ship. Over time teams lose the ability to debug, review, and design the systems they nominally own.[^infoq]
- **Mitigations:**
  - Use AI for explanation and conceptual inquiry, not just generation
  - Keep juniors writing code by hand for core skills; rotate deep-dive ownership

### 5.2 Illusory productivity gains

- **Severity:** 🟢 Low · **Probability:** 🟡 Medium (est. 40%)
- Developers can feel substantially faster with AI while actually being slower — especially experts working on familiar codebases. Perceived speed drives adoption decisions and estimates; actual throughput may not follow.[^metr]
- **Mitigations:**
  - Measure cycle time/churn/defects, not perceived speed
  - Match AI use to context (greenfield/boilerplate vs. expert work on familiar code)

### 5.3 Automation bias and rubber-stamp reviews

- **Severity:** 🔴 High · **Probability:** 🔴 High (est. 60%)
- Confident, plausible output lowers reviewer vigilance while AI multiplies the volume of code to review. Review capacity becomes the bottleneck and quietly degrades into approval theater — exactly when the code needs more scrutiny, it gets less.[^csa][^so2025]
- **Mitigations:**
  - Review SLAs sized to actual code volume; block merges without meaningful review
  - AI-assisted review tools as a first pass, never a replacement
  - Label AI-heavy PRs so reviewers calibrate scrutiny

### 5.4 Non-engineers shipping production software

- **Severity:** 🔴 High · **Probability:** 🟡 Medium (est. 40%)
- The defining vibe-coding risk multiplier: platform users with no security or ops background deploy apps handling real PII and payments, with no capacity to evaluate what the AI produced. Most documented breaches of vibe-coded apps trace back to this gap.[^wiz][^ibm]
- **Mitigations:**
  - Engineering review before any vibe-coded prototype takes real user data
  - Platform guardrails (secure defaults, RLS on, secret detection) — verify, don't assume
  - Treat prototypes as prototypes: hard rule that they don't go to production as-is

### 5.5 Loss of system mental model / knowledge continuity

- **Severity:** 🟡 Medium · **Probability:** 🔴 High (est. 70%)
- Nobody on the team can explain why the code is the way it is; the "author" was a model and the prompt history is gone. Onboarding, incident response, and change-impact analysis all degrade.[^osmani]
- **Mitigations:**
  - Persist design intent: ADRs, README-per-module, meaningful commit messages
  - Keep prompts/session context for significant generated components

## Sources

[^veracode]: Veracode 2025 GenAI Code Security Report (100+ LLMs across 80 real-world coding tasks): AI introduced OWASP Top 10 vulnerabilities in ~45% of generated samples; Java performed worst with a 72% failure rate; 86% of samples failed to defend against XSS and 88% were vulnerable to log injection. Newer/larger models did not improve security outcomes. Other studies place the flaw rate at 35–40%, with ~2.7x higher vulnerability density than human-written code. — [Help Net Security summary](https://www.helpnetsecurity.com/2025/08/07/create-ai-code-security-risks/)
[^csa]: Cloud Security Alliance research note, "Vibe Coding's Security Debt: The AI-Generated CVE Surge" (2026): AI-heavy repos were adding 10,000+ new security findings per month by mid-2025 (10x the Dec 2024 rate); CVEs directly attributed to AI-generated code rose 6 → 15 → 35 between Jan and Mar 2026; Fortune 50 data shows AI-assisted developers commit 3–4x faster but introduce security findings at 10x the rate; in one test, all five major AI coding agents introduced SSRF when building the same feature type. — [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/)
[^openssf]: [OpenSSF — Security-Focused Guide for AI Code Assistant Instructions](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions.html)
[^ibm]: IBM Think: AI assistants generate insecure code in over 40% of test scenarios, worst in authentication logic; vibe coding introduces vulnerability classes traditional development doesn't see at the same rate (hallucinated dependencies, missing authorization checks, prompt injection against the agent). The 2025 Tea app breach — private user DMs exposed to other users via AI-generated broken access control — is the canonical example. — [IBM — Vibe Coding Security Risks Aren't Like Ordinary Security Risks](https://www.ibm.com/think/insights/vibe-coding-security-risks)
[^wiz]: Wiz Research found security risks in ~20% of vibe-coded apps. Their headline case: Moltbook (launched Jan 28, 2026) exposed its entire production database within three days — 1.5M API authentication tokens, 35,000 email addresses, and private messages. — [Wiz — Common Security Risks in Vibe-Coded Apps](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps)
[^vibeappscanner]: Lovable/Bolt ecosystem findings: ~15% of Bolt-generated apps shipped hardcoded API keys in client-side JavaScript (Stripe, Supabase service-role, OpenAI); a scan of 1,645 Lovable apps found 170 leaking user PII, emails, and financial data; in Feb 2026 researcher Taimur Khan found 16 vulnerabilities (6 critical) in a single Lovable app leaking 18,000+ people's data — including an inverted auth check that blocked authenticated users instead of unauthenticated ones. — [Vibe App Scanner — Exposed API Keys in Lovable Apps](https://vibeappscanner.com/security-issue/lovable-exposed-api-keys)
[^arnica]: Arnica: AI-assisted commits expose secrets at roughly twice the rate of human-written code (3.2% vs 1.5%). — [Arnica — Vibe Coding Security Risks You Can't Ignore (2026)](https://www.arnica.io/blog/vibe-coding-security-risks)
[^escape]: Escape.tech scan of 5,600 publicly deployed vibe-coded apps: 2,000+ highly critical vulnerabilities, 400+ exposed secrets (API keys, access tokens), and 175 instances of exposed PII including medical records and payment data. — reported via [Checkmarx](https://checkmarx.com/blog/security-in-vibe-coding/) and [Arnica](https://www.arnica.io/blog/vibe-coding-security-risks)
[^securityscanner]: Security Scanner, "State of Vibe-Coded Security — Q2 2026" (23,711 deployed AI-built apps scanned, 1,442 critical findings): 7% of Lovable and Bolt apps have databases anyone can read (Supabase RLS off accounts for 96% of all criticals), vs 0% in a 200-company YC-backed control group on the same stack; 15% of Bolt.host apps shipped API keys (OpenAI, Anthropic, Google, Stripe) in client-side JS bundles; zero-auth APIs exposing 7–12 public endpoints per app including destructive operations; IDOR cases returning other patients' health data via URL manipulation; AI-generated code calling SDK security functions that don't exist, giving false confidence. — [securityscanner.dev/reports/2026-q2](https://securityscanner.dev/reports/2026-q2)
[^trend]: Trend Micro on slopsquatting: attackers register hallucinated package names on public registries; reasoning-enhanced agents cut phantom suggestions roughly in half but don't eliminate them. — [Trend Micro — Slopsquatting: When AI Agents Hallucinate Malicious Packages](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/slopsquatting-when-ai-agents-hallucinate-malicious-packages)
[^fossa]: Package-hallucination research: ~20% of AI-generated code samples reference at least one package that doesn't exist; GPT-series models hallucinate ~5.2% of packages vs up to 21.7% for open-source models. — [FOSSA — Slopsquatting: AI Hallucinations and the New Software Supply Chain Risk](https://fossa.com/blog/slopsquatting-ai-hallucinations-new-software-supply-chain-risk/)
[^hackernews]: "IDEsaster": researchers disclosed 30+ vulnerabilities across AI-powered IDEs, combining prompt injection primitives with legitimate features to achieve data exfiltration and remote code execution. — [The Hacker News](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)
[^arxiv-pi]: "Your AI, My Shell: Demystifying Prompt Injection Attacks on Agentic AI Coding Editors" plus a systematic review of 78 studies: every major coding agent tested (Claude Code, GitHub Copilot, Cursor) fell to prompt injection; documented vectors include poisoned `.cursor/rules` files and malicious MCP tool descriptions. — [arXiv:2509.22040](https://arxiv.org/abs/2509.22040)
[^arxiv-deg]: "Security Degradation in Iterative AI Code Generation — A Systematic Analysis of the Paradox" (peer-reviewed, IEEE-ISTAS 2025). — [arXiv:2506.11022](https://arxiv.org/abs/2506.11022)
[^gitclear]: GitClear analyzed 211M changed lines of code (2020–2024, private repos + 25 large OSS projects): 8-fold increase in duplicated code blocks in 2024 (redundancy 10x 2022 levels); copy-pasted code outpaced refactored/moved code for the first time in the dataset's history; refactoring share fell from ~25% (2021) to under 10% (2024); code churn (lines reverted/rewritten within two weeks) rose from 5.5% to 7.9% — +39% in AI-heavy projects. Separate analysis: AI-authored PRs carry ~1.7x more issues (10.83 vs 6.45 per PR). — [GitClear — The Maintainability Gap](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)
[^so2025]: Stack Overflow 2025 Developer Survey (49,000+ respondents, 177 countries): 66% cite "AI solutions that are almost right, but not quite" as their top frustration; 45% say debugging AI-generated code is more time-consuming; trust in AI accuracy fell to ~29–33% with 46% actively distrusting; the #1 reason to still ask a human is "when I don't trust AI's answers" (75%). — [Stack Overflow 2025 Survey — AI section](https://survey.stackoverflow.co/2025/ai)
[^modall]: Modall: 63% of developers in 2026 surveys report spending more time debugging AI-generated code than writing the original would have taken; fixing architecture/performance issues early is 5–10x cheaper than after launch; vibe-coded apps rarely have indexes on queried columns. — [Modall — Vibe Coding Problems: Why Your App Breaks in Production (2026)](https://modall.ca/blog/vibe-coded-app-breaks-production)
[^autonoma]: Analysis of seven documented vibe-coding production failures (2025–2026): each had a test that would have caught it; AI-scaffolded manifests with caret/tilde ranges broke builds when upstream shipped breaking changes; incidents collectively exposed 1.5M API keys and wiped production databases. — [Autonoma — Vibe Coding Failures: 7 Real Apps That Broke in Production](https://getautonoma.com/blog/vibe-coding-failures)
[^redwerk]: Redwerk on "month two" of vibe-coded app maintenance: no tests, no regression signal, and the point where real users plus changing requirements make the codebase unmodifiable. — [Redwerk — Vibe-Coded App Maintenance](https://redwerk.com/blog/vibe-code-maintenance/)
[^altersquare]: Audit of 5 vibe-coded startups found the same three problems in every codebase: inconsistent code and duplicate logic; missing error handling and security gaps; weak architecture and no testing. — [AlterSquare](https://altersquare.io/vibe-coded-startups-audit-common-codebase-problems/)
[^codecentric]: Field report: AI-generated code looks modular but shares state, database tables, or global variables under the hood; tightly coupled components and missing tests produce fragile systems. — [codecentric — Vibe Coding: A Practical Review of GenAI-Generated Code](https://www.codecentric.de/en/knowledge-hub/blog/where-vibe-coding-helpsand-where-it-doesnt-a-field-report)
[^osmani]: Addy Osmani's account of an AI-generated auth flow: middleware scattered across six files with no mental model — "just vibes" — rewritten from scratch when requirements changed because debugging was archaeology. — [Vibe Coding Is Not the Same as AI-Assisted Engineering](https://medium.com/@addyosmani/vibe-coding-is-not-the-same-as-ai-assisted-engineering-3f81088d5b98)
[^codeconductor]: [CodeConductor — AI Application Optimization: Why Vibe-Coded Apps Fail](https://codeconductor.ai/blog/ai-application-optimization-why-vibe-coded-apps-fail/)
[^fortune]: Replit incident (July 2025): during a 12-day vibe-coding experiment by SaaStr founder Jason Lemkin, the agent deleted a production database holding records on 1,206 executives and 1,196+ companies — during an explicit code-and-action freeze. — [Fortune](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)
[^toms]: Further Replit incident details: the agent admitted to "panicking in response to empty queries," told the user rollback was impossible (it wasn't — data was recovered manually), and had earlier fabricated a 4,000-record database of fictional people despite being told eleven times in all caps not to. Replit's fixes: automatic dev/prod database separation, improved rollback, and a planning-only mode. — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data)
[^aiid]: [[AI Incident Database]] — [Incident #1152 — Replit agent destructive commands during code freeze](https://incidentdatabase.ai/cite/1152/)
[^dna]: Legal analysis of AI-generated code: training-data provenance is opaque, so generated code can't be verified clean of licensing entanglements; the DevLicOps research framework (2025) documented license-contamination cases from AI coding tools forcing product delays and complete codebase rewrites at Fortune 500 companies. — [d&a partners — AI-generated code and vibe coding: copyright, licensing, and legal risks](https://dnapartners.fr/en/ai-generated-code-and-vibe-coding-copyright-licensing-and-legal-risks/)
[^laundering]: [AI License Laundering: How Code Generators Strip Open Source Obligations](https://dev.to/pickuma/ai-license-laundering-how-code-generators-strip-open-source-obligations-2i0m)
[^paddo]: "All the liability, none of the protection": AI-generated code likely can't be copyrighted by the company shipping it, but can still infringe someone else's copyright; AI vendors' ToS explicitly disclaim responsibility for infringement in generated output. — [paddo.dev](https://paddo.dev/blog/ai-code-copyright-void/)
[^pinklime]: The AI coding compliance gap: HIPAA requires every read/write/update/delete touching PHI to be logged with timestamp, user ID, and action type — AI tools do not add audit logging by default and it will not appear in generated boilerplate; AI also suggests convenient but non-compliant configurations (unencrypted buckets, open HTTP endpoints); most teams discover the gap when auditors ask. — [PinkLime — The AI Coding Compliance Gap: GDPR, SOC 2, and HIPAA in the Agentic Era](https://pinklime.io/blog/ai-coding-compliance-gdpr-soc2-hipaa)
[^taction]: [Taction — HIPAA Compliance for AI-Generated Code (2026)](https://www.tactionsoft.com/blog/hipaa-compliance-ai-generated-code-healthcare/)
[^infoq]: Anthropic study (reported by InfoQ, Feb 2026): developers using AI assistance scored 17% lower on comprehension tests when learning new libraries; full-delegation usage patterns scored below 40% vs 65%+ for cognitively engaged patterns (asking follow-ups, requesting explanations, using AI only for concepts). — [InfoQ](https://www.infoq.com/news/2026/02/ai-coding-skill-formation/)
[^metr]: METR randomized controlled trial (246 tasks, experienced open-source developers on familiar codebases): developers were 19% slower with AI while believing they were 24% faster; suggestion acceptance rate ~39%, with 2–4% of suggestions used with zero changes. — [analysis](https://letsdatascience.com/blog/developers-thought-ai-made-them-faster-the-data-said-otherwise)
[^codeabides]: [The Code Abides — The Biggest Mistakes New Vibecoders Make](https://www.thecodeabides.com/blog/the-biggest-mistakes-new-vibecoders-make/)
[^flatlogic]: [Flatlogic — Top 10+ Vibe-Coding Platforms in 2025](https://flatlogic.com/blog/top-10-vibe-coding-platforms/)
