#!/usr/bin/env python3
"""SSEVM page checks (free, no Claude). Owner ticked SSEVM J04, 16 Nov 2026.
C1 title form  C2 phone + no keys/tracking  C4 planning-range note.
Run: python3 tools/page-check.py   (exit 1 on any problem)"""
import re, subprocess, sys, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
pages = [p for p in subprocess.run(["git", "ls-files", "*.html"], capture_output=True, text=True).stdout.split() if p]
TITLE = re.compile(r"^.+ - v\d{2} - J\d{2} - \d{2}\.\d{2}\.\d{2} - \d{1,2}\.\d{2} (AM|PM)$")
BAD = re.compile(r"googletagmanager|google-analytics|gtag\(|fbq\(|hotjar|AIza[0-9A-Za-z_-]{20}|sk-[A-Za-z0-9]{20}|ghp_[A-Za-z0-9]{20}|api[_-]?key\s*[:=]", re.I)
problems = []
for p in pages:
    s = open(p, encoding="utf-8").read()
    m = re.search(r"<title>(.*?)</title>", s, re.S | re.I)
    t = m.group(1).strip() if m else ""
    if not TITLE.match(t):
        problems.append(f"{p}: C1 title must be 'Name - vNN - Jnn - DD.MM.YY - h.mm AM/PM' (found: '{t}')")
    if not re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*width=device-width', s, re.I):
        problems.append(f"{p}: C2 missing phone setting <meta name=\"viewport\" content=\"width=device-width,...\">")
    for b in BAD.finditer(s):
        problems.append(f"{p}: C2 key or tracking code not allowed: '{b.group(0)}'")
    if p.startswith(("plan/", "offgrid/")):
        low = s.lower()
        if "rough planning range" not in low or "qualified designer" not in low:
            problems.append(f"{p}: C4 needs the note that figures are rough planning ranges for a qualified designer to check")
for x in problems: print("PROBLEM:", x)
print(f"page check: {len(pages)} page(s), {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
