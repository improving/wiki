---
type: Reference
title: "Your Agents Have Keys. Nobody Changed the Locks."
resource: "https://driventodevelop.com/2026/08/17/your-agents-have-keys-nobody-changed-the-locks/"
author: "David O'Hara"
published: '2026-08-17'
fetched: '2026-10-17'
tags: [blog, driventodevelop.com]
---

92% of enterprise security leaders don't have full visibility into what their AI agents can access ([we already talked about how many they even know about](https://driventodevelop.com/2026/06/26/audit-clients-havent-done/)). 86% don't enforce access policies on them at all. That is not a governance problem. That is an open door.

When we onboard a new employee, we go through a checklist. Active Directory account. Role-based access. Approval chain for sensitive systems. Offboarding protocol when they leave. We do none of that for AI agents. I've been in organizations with dozens of deployed agents where nobody could tell me what those agents could access, who approved that access, or what would happen if one of them was compromised. Nobody had a list. Nobody had a policy. They had outcomes. The agents were working, so nobody asked what else they could do. Certainly, no one asked whose credentials they were using.

ServiceNow just announced it's opening its full system of action to any AI agent via MCP. That's a powerful capability. It also means the attack surface just became programmable from the outside. And if you haven't treated your agents like identities, you now have identities with no accountability model sitting at the edge of your most critical business systems.

The fix is not exotic; it's blocking-and-tackling level easy, but that doesn't mean it's getting done. Every AI agent is a non-human identity with credentials, permissions, and a blast radius if compromised. The same lifecycle that applies to human identities applies here. Provision with least privilege. Audit regularly. Revoke on change. The identity governance frameworks your teams already have are designed for exactly this problem. The gap isn't tooling. It's the assumption that agents don't need governance because they're not people. They're not. But their credentials are real, and so are the consequences.

Most enterprises have identity governance programs for humans. Almost none have extended those programs to cover machines and agents. That is the gap, and it is getting wider every week that new capabilities ship without a corresponding policy.

If one of your AI agents caused a breach tonight, how long would it take your team to trace what it had access to and revoke it? If the answer isn't "minutes," you have work to do.

[
![David O'Hara](images/Headshot---current.jpg)
](https://driventodevelop.com/author/david/)

[David O'Hara](https://driventodevelop.com/author/david/)

17 Aug 2026

[AI](https://driventodevelop.com/tag/ai/)
