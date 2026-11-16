#!/usr/bin/env python3
"""SSEVM link check (free, no Claude). Owner ticked SSEVM J04 C3, 16 Nov 2026.
Checks every link in every page and README: web links open, local files and #anchors exist.
The MSA Health link must be present in the concept plan."""
import re, subprocess, sys, os, urllib.request, urllib.error
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
files = [p for p in subprocess.run(["git", "ls-files", "*.html", "*.md"], capture_output=True, text=True).stdout.split() if p]
MSA = "https://madrasatul-muslimeen.github.io/app/"
problems, seen = [], {}
def web_ok(u):
    if u in seen: return seen[u]
    ok = False
    for method in ("HEAD", "GET"):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, method=method, headers={"User-Agent": "ssevm-link-check"}), timeout=20)
            ok = r.status < 400; break
        except urllib.error.HTTPError as e:
            if e.code in (405, 403) and method == "HEAD": continue
            break
        except Exception:
            break
    seen[u] = ok; return ok
for f in files:
    s = open(f, encoding="utf-8").read()
    links = re.findall(r'href="([^"]+)"', s) + re.findall(r'\]\(([^)\s]+)\)', s)
    ids = set(re.findall(r'id="([^"]+)"', s))
    for l in links:
        if l.startswith(("http://", "https://")):
            if not web_ok(l): problems.append(f"{f}: link does not open: {l}")
        elif l.startswith("#"):
            if l[1:] and l[1:] not in ids: problems.append(f"{f}: no section {l}")
        elif not l.startswith(("mailto:", "tel:")):
            path = os.path.normpath(os.path.join(os.path.dirname(f), l.split("#")[0]))
            if not os.path.exists(path): problems.append(f"{f}: missing file {l}")
if os.path.exists("plan/concept-plan.html") and MSA not in open("plan/concept-plan.html", encoding="utf-8").read():
    problems.append("plan/concept-plan.html: the MSA Health link is missing")
for x in problems: print("PROBLEM:", x)
print(f"link check: {len(files)} file(s), {len(seen)} web link(s), {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
