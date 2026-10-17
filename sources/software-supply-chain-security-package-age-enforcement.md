---
title: "Protecting the Software Supply Chain from Malicious Packages (+Claude Skill)"
type: "Source Summary"
description: "A 7-day minimum package age requirement closes the window between a malicious package landing and detection, packaged as a Claude skill."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, ai, improving.com]
sources:
  - "references/improving.com/software-supply-chain-security-package-age-enforcement/software-supply-chain-security-package-age-enforcement.md"
---

# Protecting the Software Supply Chain from Malicious Packages (+Claude Skill) — Summary

**Original source**: `references/improving.com/software-supply-chain-security-package-age-enforcement/software-supply-chain-security-package-age-enforcement.md`

## Summary

CVE scanners and dependency auditors only catch known vulnerabilities, leaving a window between when a malicious package lands in a registry and when the community detects and removes it. The post argues a minimum 7-day package age requirement closes that window — most malicious packages are caught within 24 to 48 hours — and packages the control as a Claude skill that provisions the correct configuration across five package managers.

## Key Claims

- Recent incidents — the axios compromise (over 100 million weekly downloads), the TanStack npm attack, and the shai-hulud Python registry attack — share one pattern, and the standard advice (audit dependencies, enable Dependabot, check lockfiles) misses the attack window.
- When a maintainer's credentials are compromised and a malicious version is published, there is no CVE entry, so no Snyk alert fires and no Dependabot PR appears; the package looks legitimate because it came from a legitimate account.
- Most published supply chain attacks are active for hours to a couple of days; a 7-day cooling-off period means a package has already survived a week of public scrutiny.
- It protects against newly published malicious versions, recently compromised maintainers, and typosquatting, but not against packages that evade detection longer than 7 days, already-locked vulnerabilities, or dependency confusion attacks.
- Implementation varies by ecosystem: pnpm (`minimumReleaseAge: 10080`, v10.16+, needs a `minimumReleaseAgeExclude` for pnpm itself), npm (a wrapper script passing a 7-day date via `--before`), Bun (`minimumReleaseAge = 604800` seconds), UV (`exclude-newer = "7 days"` in `pyproject.toml`), and NuGet (Dependabot cooldown plus exact version pinning, since native CLI support is still pending).
- pip has no native package age enforcement; the right first step is migrating to UV, which also brings speed and a more predictable resolution model.
- AI coding assistants expand the volume of dependency suggestions with no age context; an infrastructure-level control applies regardless of whether the install was typed, suggested by AI, or run by a build script.
- The skill provisions configs, a README supply chain section, and documented, auditable bypass procedures; the 7-day default can be raised to 14 or 30 days in each config file.

## Relevance

Informs [software supply chain security](/concepts/software-supply-chain-security.md), [shift-left security](/concepts/shift-left-security.md), and [application security](/concepts/application-security.md).

## Quality

Practitioner how-to by Joshua Holtz; concrete configurations and honest caveats, with a free open-source skill on GitHub.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — the Claude skill that provisions the control
- [Improving](/entities/improving.md) — hosts the skill repository and security practice
- [GitHub](/entities/github.md) — hosts the skill repo and Dependabot cooldown config

## Concepts Covered

- [software supply chain security](/concepts/software-supply-chain-security.md) — the main topic
- [shift-left security](/concepts/shift-left-security.md) — a control at install time rather than after
- [application security](/concepts/application-security.md) — one layer of a broader posture
- [AI code review](/concepts/ai-code-review.md) — AI assistants adding dependency suggestions without freshness context
