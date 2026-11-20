# bug-bounty-skills-plecitGOD

Skill metodologi **bug bounty** yang etis dan terstruktur untuk Claude Code / agen AI.
Berisi workflow pengujian keamanan yang sah, indeks cheatsheet payload/bypass,
playbook recon, lookup PoC CVE, serta referensi belajar (OWASP WSTG, Hacker101).

> ⚠️ **Hanya untuk pengujian yang diotorisasi.** Gunakan pada target yang kamu
> miliki atau yang secara eksplisit masuk scope program bug bounty / pentest.
> Verifikasi scope sebelum menguji, PoC non-destruktif, hormati rate limit &
> aturan program. Jangan menguji aset di luar scope.

## Struktur
- `SKILL.md` — definisi skill & workflow 5 fase (scope → threat model → recon → testing → report).
- `references/` — cheatsheet payload/bypass, bahan wajib (wordlist/CVE feed), learning path.
- `scripts/cve_lookup.py` — lookup PoC CVE on-demand.

## Pakai sebagai skill
Salin folder ini ke `~/.claude/skills/bug-bounty/` (atau `~/.agents/skills/bug-bounty/`).
