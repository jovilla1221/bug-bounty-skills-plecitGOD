# 🎓 Belajar & Metodologi (Study Before Testing)

Curated learning path and methodology references stored under
`/data/workspace/bug-bounty/tools/refs/`.

---

## Recommended Study Sequence

### 1. Hacker0x01/hacker101 (Official HackerOne Free Course & CTF)
- **Upstream:** `https://github.com/Hacker0x01/hacker101`
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/hacker101/`
- **Core Files:**
  - `start-here.md`: Newcomers path, Burp Suite playlist, Web Hacking & Mobile Hacking tracks, HackerOne Code of Conduct, report writing & CVSS guidance.
  - `resources.md` & `videos.md`: Recommended tools and video curriculum.
- **Practice:** Hacker101 CTF (`https://ctf.hacker101.com/`) — 26+ points unlock private program invites on HackerOne.

### 2. nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters (Beginner Roadmap)
- **Upstream:** `https://github.com/nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters`
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/Resources-for-Beginner-Bug-Bounty-Hunters/`
- **Core Modules (`assets/`):**
  - `basics.md`, `setup.md`, `tools.md` — HTTP basics, proxy setup, recon workflow
  - `vulns.md` — Vulnerability breakdowns with writeups
  - `labs.md` — Safe practice platforms
  - `blogposts.md`, `talks.md`, `books.md`, `coding.md`, `mobile.md`, `health.md`

### 3. OWASP/wstg (Web Application Security Testing Standard)
- **Upstream:** `https://github.com/OWASP/wstg` (CC-BY-SA)
- **Local Sparse Checkout:** `/data/workspace/bug-bounty/tools/refs/wstg/document/4-Web_Application_Security_Testing/`
- **14 Testing Domains:**
  - `01-Information_Gathering`
  - `02-Configuration_and_Deployment_Management`
  - `03-Identity_Management`
  - `04-Authentication`
  - `05-Authorization`
  - `06-Session_Management`
  - `07-Injection`
  - `08-Error_Handling`
  - `09-Weak_Cryptography`
  - `10-Business_Logic`
  - `11-Client-side`
  - `12-API_Testing`
  - `13-WebAssembly_Testing`
- Pairs directly with `/data/workspace/bug-bounty/methodologies/owasp_wstg_checklist.md`.

### 4. qazbnm456/awesome-web-security (Curated Web Security Knowledge Index)
- **Upstream:** `https://github.com/qazbnm456/awesome-web-security`
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/awesome-web-security/`
- **Features:**
  - Structured topic catalog (`README.md` & `data/index.json`) covering XSS, SQLi, CSRF, SSRF, XXE, OAuth/JWT, Prototype Pollution, Deserialization, SAML, Cache Poisoning, WAF/CSP evasion, Recon, and CTF writeups.
  - Also includes its own skill definition at `skills/awesome-web-security/SKILL.md`.

### 5. HackTricks-wiki/hacktricks (Deep Exploitation Encyclopedia)
- **Upstream:** `https://github.com/HackTricks-wiki/hacktricks`
- **Local Sparse Checkout:** `/data/workspace/bug-bounty/tools/refs/hacktricks/src/pentesting-web/`
- **Key Web Topics Available Locally:**
  - `idor.md`, `2fa-bypass.md`, `403-and-401-bypasses.md`, `account-takeover.md`
  - `hacking-jwt-json-web-tokens.md`, `cors-bypass.md`, `crlf-0d-0a.md`
  - `http-request-smuggling/`, `cache-deception/`, `content-security-policy-csp-bypass/`
  - `file-inclusion/`, `file-upload/`, `deserialization/`, `business-logic-vulnerabilities.md`
  - `abusing-hop-by-hop-headers.md`, `client-side-path-traversal.md`, `domain-subdomain-takeover.md`

### 6. vavkamil/awesome-bugbounty-tools (Tooling Catalog)
- **Upstream:** `https://github.com/vavkamil/awesome-bugbounty-tools` (CC0)
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/awesome-bugbounty-tools/README.md`
- **Categories Covered:**
  - **Recon:** Subdomain enum (`subfinder`, `amass`, `puredns`, `dnsx`), port scanning (`naabu`, `masscan`, `nmap`), screenshots, tech fingerprinting, content discovery, JS/links, parameters, WAF evasion.
  - **Exploitation:** Command injection, CORS, CRLF, GraphQL, IDOR, Open Redirect, Race Condition, Request Smuggling, SSRF, SQLi, XSS, XXE, Cache Poisoning.
  - **Misc:** Secrets, Git, Buckets, JWT, `postMessage`, Subdomain Takeover, 403 bypass.
