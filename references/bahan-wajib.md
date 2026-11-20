# 📚 Bahan Wajib (Wordlists, Payloads, Cheatsheets & Feeds)

Curated reference inventory stored locally under `/data/workspace/bug-bounty/tools/refs/`
(with on-demand lookup for massive repositories like `trickest/cve` and additional `SecLists` files).

---

## 1. danielmiessler/SecLists (Wordlists: Fuzzing, Discovery, Payloads)
- **Upstream:** `https://github.com/danielmiessler/SecLists` (MIT)
- **Local Sparse Checkout:** `/data/workspace/bug-bounty/tools/refs/SecLists/`

### Locally Checked-Out Essential Wordlists
| Purpose | Local Path (under `/data/workspace/bug-bounty/tools/refs/SecLists/`) |
| :--- | :--- |
| Common web directories/files | `Discovery/Web-Content/common.txt` |
| Small directory bruteforce | `Discovery/Web-Content/raft-small-directories.txt` |
| Small file bruteforce | `Discovery/Web-Content/raft-small-files.txt` |
| Quick high-value endpoints | `Discovery/Web-Content/quickhits.txt` |
| API endpoints | `Discovery/Web-Content/api/api-endpoints.txt` |
| Parameter discovery (Burp list) | `Discovery/Web-Content/burp-parameter-names.txt` |
| Subdomains (top 5000) | `Discovery/DNS/subdomains-top1million-5000.txt` |
| XSS payloads (robot-friendly) | `Fuzzing/XSS/robot-friendly/XSS-Jhaddix.txt` |
| XSS polyglots | `Fuzzing/Polyglots/XSS-Polyglot.txt` |
| LFI / path traversal | `Fuzzing/LFI/LFI-Jhaddix.txt` |
| SQL injection | `Fuzzing/SQLi/Generic-SQLi.txt`, `Fuzzing/SQLi/quick-SQLi.txt` |
| Command injection | `Fuzzing/command-injection-commix.txt` |
| SSTI special vars | `Fuzzing/template-engines-special-vars.txt` |

To add more lists from `SecLists` on demand without cloning the full 3.7 GB repo:
```bash
cd /data/workspace/bug-bounty/tools/refs/SecLists
git sparse-checkout add <relative/path/to/list.txt>
```

---

## 2. daffainfo/AllAboutBugBounty (Bypasses, Payloads & Tech Notes)
- **Upstream:** `https://github.com/daffainfo/AllAboutBugBounty`
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/AllAboutBugBounty/`
- **Key Sections:**
  - **Bypasses (`Bypass/`):** `Bypass 2FA.md`, `Bypass 403.md`, `Bypass 429.md`, `Bypass Captcha.md`
  - **Vulnerabilities:** `Insecure Direct Object References.md`, `Server Side Request Forgery.md`, `OAuth Misconfiguration.md`, `Cross Site Scripting.md`, `SQL Injection.md`, `NoSQL Injection.md`, `CRLF Injection.md`, `Host Header Injection.md`, `Mass Assignment.md`, `Web Cache Deception.md`, `Web Cache Poisoning.md`, `Arbitrary File Upload.md`, `Open Redirect.md`
  - **Checklists & Misc:** `Checklist/Forgot Password.md`, `Misc/Account Takeover.md`, `Misc/JWT Vulnerabilities.md`, `Misc/Business Logic Errors.md`, `Misc/Exposed API keys.md`
  - **Technologies (`Technologies/`):** Apache, Confluence, Grafana, HAProxy, Jenkins, Jira, Joomla, Laravel, Moodle, Nginx, WordPress, Zend
  - **Reconnaissance (`Reconnaissance/`):** `Scope.md`, `Github Dorks.md`, `Google Dorks.md`, `Shodan Dorks.md`

---

## 3. EdOverflow/bugbounty-cheatsheet (Tricks & Exploitation Snippets)
- **Upstream:** `https://github.com/EdOverflow/bugbounty-cheatsheet` (CC-BY-SA)
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/bugbounty-cheatsheet/`
- **Key Cheatsheets (`cheatsheets/`):**
  - `bugbountytips.md` (Git recon, GitLab `/explore`, IDOR->XSS->ATO, POST->GET CSRF escalation)
  - `ssrf.md`, `xss.md`, `sqli.md`, `lfi.md`, `rce.md`, `xxe.md`, `xslt.md`, `template-injection.md`
  - `cors.md`, `crlf.md`, `open-redirect.md`, `content-injection.md`, `csv-injection.md`, `recon.md`

---

## 4. LasCC/HackTools (All-in-One Browser Extension Payloads)
- **Upstream:** `https://github.com/LasCC/HackTools`
- **Local Sparse Checkout:** `/data/workspace/bug-bounty/tools/refs/HackTools/src/`
- **Key Payload & Component Sources:**
  - `src/assets/data/Payloads.json` (msfvenom / shell payload templates)
  - `src/assets/data/RevShell.json` & `src/assets/data/Encoder.json`
  - `src/components/web/` (`XSS.tsx`, `SqlInjection.tsx`, `LFI.tsx`, `PhpReverseShell.tsx`)
  - `src/components/encoding/` (`URLEncode.tsx`, `HexEncode.tsx`, `DataEncoding.tsx`, `Hashing.tsx`)

---

## 5. jakejarvis/awesome-shodan-queries (Shodan Reconnaissance Queries)
- **Upstream:** `https://github.com/jakejarvis/awesome-shodan-queries` (CC0)
- **Local Clone:** `/data/workspace/bug-bounty/tools/refs/awesome-shodan-queries/readme.md`
- **How to Use for Authorized Scope Only:**
  Always append scope-narrowing filters such as `org:"Target Org"`, `hostname:"target.com"`, or `net:x.x.x.x/xx` to avoid touching third-party assets.
  Also pair with `/data/workspace/bug-bounty/tools/refs/AllAboutBugBounty/Reconnaissance/Shodan Dorks.md` for bug-bounty-focused queries (`ssl.cert.subject.cn`, `http.title`, exposed dashboards).

---

## 6. trickest/cve (Latest CVE Feed + Public PoCs)
- **Upstream:** `https://github.com/trickest/cve` (MIT)
- **Access Pattern (On-Demand — avoids 925 MB local clone):**
  Use the helper script `/data/home/.agents/skills/bug-bounty/scripts/cve_lookup.py`:
  ```bash
  python3 /data/home/.agents/skills/bug-bounty/scripts/cve_lookup.py CVE-2024-3094
  ```
  Or fetch directly via raw GitHub URL:
  `https://raw.githubusercontent.com/trickest/cve/main/<YEAR>/<CVE-ID>.md`
