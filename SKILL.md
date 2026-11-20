---
name: bug-bounty
description: >-
  Authorized bug bounty hunter workflow, curated payload/bypass cheatsheets,
  wordlist index, recon playbooks, CVE PoC lookup, and OWASP WSTG / Hacker101
  learning references. Use when conducting authorized bug bounty reconnaissance,
  scope verification, web/API vulnerability testing, bypass/payload lookup,
  or writing triage-ready vulnerability reports.
---

# Bug Bounty Hunter Skill

Structured, ethical, hypothesis-driven bug bounty methodology built around your
curated **Bahan Wajib** (wordlists, payloads, cheatsheets, CVE feeds) and
**Belajar** (methodology & training) repositories.

---

## Mandatory Guardrails (Non-Negotiable)

1. **Strict Scope Verification First**: Before touching any domain, IP, or endpoint,
   verify it against the program's scope file using
   [scope_checker.py](/data/workspace/bug-bounty/scripts/scope_checker.py):
   ```bash
   python3 /data/workspace/bug-bounty/scripts/scope_checker.py <scope.txt> <target>
   ```
   Never test, scan, or probe out-of-scope assets.
2. **Non-Destructive Proof of Concept Only**: Stop immediately once impact is
   proven. Never modify/delete production data, exfiltrate real user PII, pivot
   into internal networks, or run disruptive/DoS traffic.
3. **Respect Rate Limits & Program Rules**: Honor platform headers, custom
   User-Agent requirements, and test-account rules.
4. **Authorized Context Only**: Decline requests to target unowned systems
   without clear bug bounty / pentest authorization.

---

## Operational Workflow (5 Phases)

### Phase 1 — Scope & Program Rules
- Scaffold the target workspace automatically with:
  ```bash
  python3 /data/workspace/bug-bounty/scripts/new_target.py <program> --platform HackerOne
  ```
  This creates `/data/workspace/bug-bounty/targets/<program>/` (`scope.txt`, `recon/`, `findings/`, target & recon notes) and links it in `/data/workspace/bug-bounty/00 - Second Brain.md`.
- Validate every target host/URL with `scope_checker.py`.
- Note excluded vulnerability classes (e.g., self-XSS, missing headers without impact, rate-limit on non-sensitive forms).

### Phase 2 — Study & Threat Model Before Testing
- Review foundational methodology in [learning-path.md](./references/learning-path.md)
  (Hacker101, OWASP WSTG, HackTricks, NahamSec Beginner Resources, Awesome Web Security).
- Follow `/data/workspace/bug-bounty/methodologies/owasp_wstg_checklist.md`.
- Map the tech stack, auth model (cookies/JWT/OAuth), roles/tenants, and high-value business flows.

### Phase 3 — Reconnaissance & Asset Discovery
- Use curated wordlists from local `SecLists` sparse checkout (`/data/workspace/bug-bounty/tools/refs/SecLists/`)
  and query patterns in [bahan-wajib.md](./references/bahan-wajib.md).
- Run passive recon first (Certificate Transparency / `certspotter`, Shodan dorks from `awesome-shodan-queries`, GitHub dorks, JS endpoint extraction).
- When fingerprinting known software versions, look up recent CVE PoCs using:
  ```bash
  python3 /data/home/.agents/skills/bug-bounty/scripts/cve_lookup.py CVE-2021-41773
  ```

### Phase 4 — Hypothesis-Driven Vulnerability Testing
Prioritize high-impact logic and authorization bugs before noisy fuzzing:
1. **Access Control**: IDOR / BOLA, horizontal & vertical privilege escalation, multi-tenant isolation.
2. **Authentication & Session**: OAuth misconfigurations, JWT (`alg: none`, RS256->HS256, weak secrets), password reset & 2FA bypasses, account takeover chains.
3. **Injection & Server-Side**: SSRF (cloud metadata, IP encoding bypasses), SQLi/NoSQLi, SSTI, LFI/path traversal, command injection.
4. **HTTP / Cache / Client-Side**: 403/429 bypasses, Web Cache Poisoning & Deception, CORS misconfiguration, XSS, CSRF, Open Redirect, CRLF.
5. **Business Logic**: Race conditions, price/quantity tampering, step skipping.

Consult [payloads-and-bypasses.md](./references/payloads-and-bypasses.md) and the local
cloned repositories in `/data/workspace/bug-bounty/tools/refs/` for exact payloads and WAF bypasses.

### Phase 5 — Verification & Reporting
- Confirm reproducibility cleanly with minimal PoC steps (two test accounts for IDOR/auth issues).
- Draft the report using `/data/workspace/bug-bounty/templates/report_template.md`
  with clear impact, CVSS v3.1 vector, raw HTTP request/response PoC, and remediation guidance.

---

## Reference Index

| File | Contents |
| :--- | :--- |
| [bahan-wajib.md](./references/bahan-wajib.md) | 6 core resource repos: SecLists (local paths), AllAboutBugBounty, bugbounty-cheatsheet, HackTools, awesome-shodan-queries, trickest/cve |
| [learning-path.md](./references/learning-path.md) | 6 learning & methodology repos: Hacker101, awesome-web-security, HackTricks, NahamSec Beginner Resources, OWASP WSTG, awesome-bugbounty-tools |
| [payloads-and-bypasses.md](./references/payloads-and-bypasses.md) | Distilled practical cheatsheet for recon, bypasses (403/429/2FA), IDOR, SSRF, OAuth/JWT, XSS, CORS, cache, and injection checks |
| [cve_lookup.py](./scripts/cve_lookup.py) | On-demand CLI fetcher for `trickest/cve` PoC markdown files |
