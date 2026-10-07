"""Builds assets/stats.svg from the GitHub API (stdlib only). Run by the workflow."""
import json, os, urllib.request, datetime, collections
USER = os.environ.get("GH_USER", "masked-shinobi")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "stats.svg")
RED, CY, VI = "#ff2e4d", "#00e5ff", "#b36bff"
PAL = [RED, CY, VI, "#3dff9a", "#ffb02e", "#5b8cff", "#ff6bd5", "#8b8b99"]
FS = "'Inter','Segoe UI',-apple-system,Helvetica,Arial,sans-serif"
FM = "'JetBrains Mono','SF Mono',Menlo,Consolas,monospace"

def api(path):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if os.environ.get("GITHUB_TOKEN"): h["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    return json.load(urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=h), timeout=25))

try:
    u = api(f"/users/{USER}")
    repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in repos); forks = sum(r["forks_count"] for r in repos)
    langs = collections.Counter(r["language"] for r in repos if r["language"])
    nums = [(str(u["public_repos"]), "Public repos", RED), (str(stars), "Stars earned", CY),
            (str(u["followers"]), "Followers", VI), (str(forks), "Forks", RED)]
except Exception as e:
    print("API failed, using fallback:", e)
    nums = [("18", "Public repos", RED), ("0", "Stars earned", CY), ("0", "Followers", VI), ("0", "Forks", RED)]
    langs = collections.Counter({"JavaScript": 6, "Python": 5, "C++": 2, "Kotlin": 1, "Solidity": 1, "CSS": 1})

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;")
def T(x, y, s, size, fill, font=FS, w=400, a="start", ls=0):
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}" letter-spacing="{ls}">{esc(s)}</text>'
def tile(x, y, w, h, c):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#0c0c0f" stroke="#23232b"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="url(#g{PAL.index(c)})"/>')
H = 264
defs = "".join(f'<radialGradient id="g{i}" cx="0" cy="0" r="1"><stop offset="0" stop-color="{c}" stop-opacity=".17"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for i, c in enumerate(PAL))
s = f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H}" viewBox="0 0 1000 {H}" fill="none"><defs>{defs}</defs><rect width="1000" height="{H}" rx="22" fill="#050505"/>'
for i, (n, l, c) in enumerate(nums):
    x = i * 253
    s += tile(x, 0, 241, 110, c) + T(x + 24, 62, n, 46, c, FS, 800) + T(x + 24, 92, l, 12, "#8b8b99", FM)
s += tile(0, 122, 1000, 142, VI) + T(28, 158, "// TOP_LANGUAGES", 11, VI, FM, 700, ls=2)
tot = sum(langs.values()) or 1; x = 28; bw = 944; items = langs.most_common(8)
for i, (n, v) in enumerate(items):
    w = max(6, bw * v / tot)
    s += f'<rect x="{x:.1f}" y="174" width="{w:.1f}" height="14" rx="3" fill="{PAL[i%8]}"/>'; x += w + 0
for i, (n, v) in enumerate(items):
    cx = 28 + (i % 4) * 236; cy = 220 + (i // 4) * 24
    s += f'<circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{PAL[i%8]}"/>' + T(cx + 18, cy, f"{n}  {v*100/tot:.0f}%", 12, "#c9c9d1", FM)
s += T(972, 158, "updated " + datetime.date.today().isoformat(), 10.5, "#8b8b99", FM, 400, "end") + "</svg>"
open(OUT, "w").write(s); print("wrote", OUT)
