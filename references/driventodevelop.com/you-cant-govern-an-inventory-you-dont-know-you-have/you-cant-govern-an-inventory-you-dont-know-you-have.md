---
type: Reference
title: "You Cant Govern an Inventory You Dont Know You Have"
resource: "https://driventodevelop.com/2026/08/21/you-cant-govern-an-inventory-you-dont-know-you-have/"
author: "David O'Hara"
published: '2026-08-21'
fetched: '2026-10-17'
tags: [blog, driventodevelop.com]
---

Nobody in your organization knows exactly how many AI agents are running right now. I am not guessing. OutSystems surveyed nearly 1,900 IT leaders and found that 96% of enterprises are running agents. Only 12% have a centralized platform to manage any of it.

I have been writing about the identity governance layer of this problem (the access and permissions side is what I covered in [Your Agents Have Keys. Nobody Changed the Locks.](https://driventodevelop.com/2026/08/17/your-agents-have-keys-nobody-changed-the-locks/)). But there is a step that comes before identity governance that most organizations are skipping entirely: inventory. You cannot govern what you do not know exists.

Here is how this plays out in practice. Agent deployment happened at the team level, not the enterprise level. A department built a custom agent. A vendor pre-loaded one as a feature. An automation tool spun one up during implementation. Nobody registered any of it centrally because there was no central registration process. So now you have 96% adoption and 12% visibility, and the 92% gap is not theoretical risk. It is agents operating in your environment, connected to your systems, with permissions nobody audited, owned by nobody accountable.

The fix is not a new tool. It is a policy that says: before any agent goes into production in this organization, it gets registered, named, assigned an owner, and documented for what it can access. That is it. That is the Agentic Landing Zone. Not a platform purchase. A decision that the next agent does not go live until someone can answer three questions: what does it do, what can it touch, and who is responsible when something goes wrong.

Does your organization have a list of every AI agent currently running in production? If the honest answer is no, that is where governance starts.

[
![David O'Hara](images/Headshot---current.jpg)
](https://driventodevelop.com/author/david/)

[David O'Hara](https://driventodevelop.com/author/david/)

21 Aug 2026

[systems thinking](https://driventodevelop.com/tag/systems-thinking/)
