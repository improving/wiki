---
type: Reference
title: "Security: The Thing That Everyone Loves to Hate"
resource: "https://www.improving.com/thoughts/security-the-thing-that-everyone-loves-to-hate/"
author: "Sonali Srivastava"
published: '2026-01-14'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Security often gets pushed to 'later' in cloud native development as teams rush to ship features, optimize costs, or scale faster. However, incidents like [Log4j](https://www.ibm.com/think/topics/log4j) (an OSS program behind the 34% increase in vulnerability exploitation between 2020 and 2021) have shown that “later” usually means crisis mode, late-night calls, patching under pressure, and scrambling to contain the damage.

The truth is that cloud native security is as much about how teams think, collaborate, and prioritize it as it is about tools or compliance checklists. And here lies the real challenge: security is still seen as someone else’s problem. Due to this, 50% of organizations now have critical security debt, high-severity issues left open for more than 1 year, according to [ITPO](https://www.itprotoday.com/software-development/software-development-teams-struggle-as-security-debt-reaches-critical-levels). Developers focus on shipping, product managers focus on revenue, and platform engineers juggle complexity, while security risks quietly pile up.

At KubeCon + CloudNativeCon India 2025, I, [Sonali Srivastava](https://www.linkedin.com/in/sonali-srivastava-530782ab/), brought together a panel of cloud native experts. [Ram Iyengar](https://www.linkedin.com/in/ram-iyengar/), [Bhavani Indukuri](https://www.linkedin.com/in/bhavani-indukuri-994470114/), [Anusha Hegde](https://www.linkedin.com/in/anusha-hegde-6468897a/), and I took this challenge head-on to spread awareness about prioritizing security. Our message was clear: to build truly resilient systems, security must be everyone’s responsibility, baked into the culture from day one, not bolted at the end.

In this blog post, we will explore how security spans differently across roles and why understanding these perspectives is essential for building a security-first organization. From spotting new-age threats like QR phishing to shifting security left in the SDLC and building a culture where accountability replaces blame.

## Wake-up Call: New Threats and Everyday Risks

Security threats today evolve faster than awareness. Attack vectors are no longer limited to traditional phishing or endpoint breaches, rather they are dynamic, social, and increasingly AI-driven.

Some of the emerging threats are:

- **Quishing or QR phishing **where users are tricked into scanning malicious QR codes during daily activities like making a payment, checking restaurant menu or opening a URL by scanning a QR code that can compromise devices or accounts.
- **Prompt injection attacks** targeting LLM-integrated applications, manipulating AI systems to reveal sensitive data.
- **Jailbreaks**, bypass model restrictions or gain elevated access in sandboxed environments.
- **Dependency confusion attacks**, where attackers exploit package naming conventions to insert malicious code into supply chains.
- **Configuration drift exploits**, where unsupervised or AI generated code changes in cloud infrastructure create unintentional vulnerabilities.

The threat landscape is expanding faster than organizational readiness. Security awareness, tooling, and culture must evolve just as quickly by working on the foundation.

## Security Through Different Lenses

### **Developers' Lens: Simplicity and Early Detection**

Developers are often caught between the pressure to deliver fast and the need to maintain secure practices. The reality is that every dependency added, every library imported, and every image chosen introduces potential risk.

**What developers can focus on:**

- **Simplify the stack**: Fewer dependencies mean fewer unknowns and lower vulnerability risk. Question every third-party library before adding it to your project.
- **Use simple base images**: Complex base images bring unnecessary packages that expand your attack surface.
- **Integrate SBOMs early**: Software Bill of Materials (SBOM) generation should be part of your build process, not an afterthought.
- **Enforce security at PR stage**: Use security linters in your IDE and make vulnerability checks a standard part of code reviews.

*"You should think of having less dependencies when you are trying to choose your base images. That's where SBOMs are really important." - Bhavani Indukuri *

A developer’s role is to make choices that minimize the blast radius of failures.

### **Security Engineer's Lens: Discipline Over Band-Aids**

Security engineers often get painted as the "people who say no," but their perspective is about building sustainable practices that prevent recurring issues rather than applying quick fixes.

**What security engineers can focus on:**

- **Treat governance as discipline, not bureaucracy**: Frameworks like Pod Security Standards (PSS) and compliance requirements like GDPR aren't obstacles. They're guardrails that create consistent, repeatable patterns for secure delivery.
- **Build resilience through prevention**: The goal isn't just passing audits; it's creating systems that make insecure configurations difficult to deploy in the first place.
- **Establish security gates**: Automated checks that prevent vulnerable code from reaching production should be non-negotiable, not optional.

*"There are governances and compliances in place for a reason; it's like when you used to go to school, you used to stand in a straight line." - Sonali Srivastava *

Security engineers shape the right habits from the start, making security the path of least resistance rather than an additional burden.

### **Product Managers' Lens: Security as Strategic Investment**

Product managers face constant tension between security and speed. The temptation is to treat security as "tech debt", something to be addressed later when there's time. But this framing is fundamentally flawed. [Average fix time for security flaws has increased 47% in five years (from 171 to 252 days)](https://www.itprotoday.com/software-development/software-development-teams-struggle-as-security-debt-reaches-critical-levels), as per ITPO.

**What product managers can focus on:**

- **Reframe security as a product feature**: Security isn't just a technical concern; it's tied directly to trust, reliability, and brand reputation. Insecure products lose customers.
- **Prioritize security alongside features**: Include security requirements in feature specs from day one. Security debt compounds faster than technical debt.
- **Understand different risk types**: Vulnerabilities (known CVEs in dependencies) and misconfigurations (policy violations, access control issues) are distinct problems requiring different approaches.
- **Use the right tools for visibility**: Tools like VEX (Vulnerability Exploitability eXchange) help manage vulnerabilities, while [policy engines like Kyverno](https://www.infracloud.io/kyverno-consulting-support/) address misconfigurations.

*"You have vulnerabilities which is a whole big class of problems... The other class of problems is misconfigurations." - Anusha Hegde *

Once PMs factor security into roadmap decisions, it stops being a last-minute scramble and becomes a competitive advantage.

### **DevOps/Platform Engineers' Lens: Infrastructure as Security Boundary**

[Platform engineers](https://www.infracloud.io/platform-engineering-consulting/) sit at the intersection of development velocity and operational stability. Their decisions around infrastructure, access controls, and automation directly impact an organization's security posture.

**What platform engineers can focus on:**

- **Enforce security through automation**: Security policies shouldn't rely on manual checks. Automated gates ensure that insecure configurations never make it to production.
- **Maintain least-privilege access**: Regularly audit and rotate credentials. Over-permissioned accounts are one of the most common attack vectors.
- **Manage configuration drift**: Unsupervised changes in cloud infrastructure create unintentional vulnerabilities. Use infrastructure-as-code and policy enforcement to prevent drifts.
- **Build observability into security**: Integrate security metrics and dashboards into daily workflows, so issues are visible before they become incidents.

Platform engineers create the infrastructure that makes security scalable, or they create the gaps that attackers exploit.

### **Leadership's Lens: Culture and Accountability**

Leadership sets the tone for whether security is genuinely valued or just performative. Without executive buy-in, security initiatives struggle to get resources, attention, or cultural traction.

**What leadership can focus on:**

- **Allocate time for security**: Dedicate sprint capacity to security improvements, not just feature work. Security isn't free; it requires investment.
- **Tie security to customer trust:** Treat security incidents as customer-impact events, not just technical failures. If there's a vulnerability, users lose trust in product; the product loses users and eventually surfaces as revenue loss.
- **Celebrate proactive security**: Recognize teams who catch vulnerabilities early or improve security posture. What gets rewarded gets repeated.
- **Make security visible**: Review security metrics alongside customer satisfaction, retention, and revenue. What gets measured gets managed.
- **Foster psychological safety**: Create an environment where people can report issues without fear. Blame-driven cultures hide problems until they explode.

Leadership’s job is to create conditions where security thrives across the organization.

## Building a Security-first Culture

Understanding these different perspectives is just the starting point. The real challenge is weaving them together into a cohesive culture where security is a priority.

- **Educate and empower**: Make security training part of onboarding and continuous learning for all team members.
- **Normalize ownership**: Encourage every role, developer, PM, or DevOps engineer, to think like a security enthusiast.
- **Create feedback loops**: Turn post-incident reviews into actionable learning opportunities, not blame sessions.
- **Make it visible**: Integrate security metrics and dashboards into daily workflows to reinforce awareness.
- **Focus on Adaptability:** View security first culture as a strategic asset that must be actively managed and adjusted as the technology landscape changes or new threats and strategies emerge.

A multi-layered defense approach complements this culture, promoting protection across applications, infrastructure, and organizational boundaries. Security is a shared responsibility that comes from anticipating risk and building systems to prevent, detect, and contain threats.

## Next Step: The Cultural Transformation

The threat landscape continues to evolve. AI-driven attacks, supply chain vulnerabilities, and configuration exploits are becoming more sophisticated. Organizations can find their way to security only with cultural transformation.

Security must be embedded into daily workflows and maintained through transparency. When security becomes a shared conversation rather than a compliance checkbox, that's when real organizational maturity begins. From silos and finger-pointing to trust and collaboration, organizations move from reactive fixes to proactive resilience.

Each issue should be treated as an opportunity to identify gaps, strengthen systems, and ensure that the same vulnerabilities don't resurface. This mindset builds not just stronger systems, but more mature organizations. At Improving, trust is at the core of everything we do, and keeping software secure is critical to keeping the trust. The consistent focus on security and privacy is the reason why so many enterprises trust us as one of the [best software consulting providers](https://www.improving.com/contact/).
