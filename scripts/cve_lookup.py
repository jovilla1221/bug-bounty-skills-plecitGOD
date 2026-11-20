#!/usr/bin/env python3
"""
Fetch CVE details and public PoC references on demand from trickest/cve.
Avoids storing the ~925 MB repository locally.
"""

import re
import sys
import urllib.error
import urllib.request


def fetch_cve(cve_id: str) -> str:
    cve_id = cve_id.strip().upper()
    match = re.fullmatch(r"CVE-(\d{4})-(\d{4,})", cve_id)
    if not match:
        raise ValueError(f"Invalid CVE ID format: {cve_id} (expected CVE-YYYY-NNNN)")

    year = match.group(1)
    url = f"https://raw.githubusercontent.com/trickest/cve/main/{year}/{cve_id}.md"
    req = urllib.request.Request(url, headers={"User-Agent": "bug-bounty-skill/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 cve_lookup.py <CVE-YYYY-NNNN>", file=sys.stderr)
        return 1

    cve_id = sys.argv[1]
    try:
        content = fetch_cve(cve_id)
        print(content)
        return 0
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    except urllib.error.HTTPError as exc:
        print(f"[NOT FOUND] {cve_id} returned HTTP {exc.code} from trickest/cve", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"[ERROR] Failed to fetch {cve_id}: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
