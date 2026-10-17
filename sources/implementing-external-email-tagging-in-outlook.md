---
title: "Implementing External Email Tagging in Outlook"
type: "Source Summary"
description: "A PowerShell how-to for enabling Outlook's External sender tag in Exchange Online to help users spot phishing from outside the organization."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, microsoft, improving.com]
sources:
  - "references/improving.com/implementing-external-email-tagging-in-outlook/implementing-external-email-tagging-in-outlook.md"
---

# Implementing External Email Tagging in Outlook — Summary

**Original source**: `references/improving.com/implementing-external-email-tagging-in-outlook/implementing-external-email-tagging-in-outlook.md`

## Summary

Carlos Tanseco explains how to enable Microsoft's "External" tag identifier, which labels email from outside the organization to help users spot spam and phishing. The feature is off by default and is turned on through Exchange Online PowerShell. The post gives the exact commands, allow-list options, and a caveat about propagation time.

## Key Claims

- The External tag appears in Outlook on the web, Mac, iOS, and Android; clicking it reveals the sender's address.
- In Outlook for Windows clients the tag shows as a mail tip in the reading pane, with an option to block the sender.
- Enable it organization-wide with `Set-ExternalInOutlook -Enabled $true` after importing the ExchangeOnlineManagement module and connecting as an admin.
- Specific senders or whole domains can be allow-listed via `Set-ExternalInOutlook -AllowList`.
- Adding one domain at a time may throw an exception; adding two at a time is a suggested workaround.
- Verify with `Get-ExternalInOutlook`; expect 24–48 hours before the tag starts appearing.

## Relevance

A defensive configuration step supporting [zero trust security](/concepts/zero-trust-security.md) and a [security culture](/concepts/security-culture.md) where users help identify external threats in the [Microsoft](/entities/microsoft.md) estate.

## Quality

Practical admin tutorial by Carlos Tanseco; accurate and reproducible, but narrow in scope and limited to Microsoft 365.

## Entities Mentioned

- [Microsoft](/entities/microsoft.md) — owner of the Outlook/Exchange feature
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [zero trust security](/concepts/zero-trust-security.md) — verify rather than trust by default
- [security culture](/concepts/security-culture.md) — making security everyone's job
- [application security](/concepts/application-security.md) — reducing phishing exposure
