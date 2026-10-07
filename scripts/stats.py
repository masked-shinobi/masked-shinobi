"""Builds assets/stats-dark.svg + stats-light.svg from the GitHub API (stdlib only)."""
import json, os, datetime, collections, urllib.request
from gen import THEMES, T, svg, card, write, FM, USER as DEFAULT_USER

USER = os.environ.get("GH_USER", DEFAULT_USER)

def api(path):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if os.environ.get("GITHUB_TOKEN"): h["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    return json.load(urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=h), timeout=25))

def fetch():
    try:
        u = api(f"/users/{USER}")
        repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
        langs = collections.Counter(r["language"] for r in repos if r["language"])
        return [(str(u["public_repos"]), "PUBLIC REPOS"), (str(sum(r["stargazers_count"] for r in repos)), "STARS EARNED"),
                (str(u["followers"]), "FOLLOWERS"), (str(sum(r["forks_count"] for r in repos)), "FORKS")], langs
    except Exception as e:
        print("API failed, using fallback:", e)
        return ([("18", "PUBLIC REPOS"), ("0", "STARS EARNED"), ("0", "FOLLOWERS"), ("0", "FORKS")],
                collections.Counter({"JavaScript": 6, "Python": 5, "C++": 2, "Kotlin": 1, "Solidity": 1, "CSS": 1}))

def build(t, nums, langs):
    pal = t["a"] + t["extra"]; b = ""
    for i, (n, l) in enumerate(nums):
        x = i * 252
        b += card(t, x, 0, 244, 112, i) + T(t, x + 24, 64, n, 46, t["a"][i], w=800) + T(t, x + 24, 92, l, 10.5, t["mut"], FM, 700, ls=1.5)
    b += card(t, 0, 128, 1000, 140, 0)
    b += T(t, 28, 162, "TOP LANGUAGES", 11, t["a"][0], FM, 700, ls=2) + T(t, 972, 162, "updated " + datetime.date.today().isoformat(), 10.5, t["mut"], FM, a="end")
    tot = sum(langs.values()) or 1; items = langs.most_common(8); x = 28
    b += '<clipPath id="c"><rect x="28" y="176" width="944" height="12" rx="6"/></clipPath><g clip-path="url(#c)">'
    for i, (n, v) in enumerate(items):
        w = 944 * v / tot; b += f'<rect x="{x:.1f}" y="176" width="{w+1:.1f}" height="12" fill="{pal[i]}"/>'; x += w
    b += "</g>"
    for i, (n, v) in enumerate(items):
        cx, cy = 28 + (i % 4) * 236, 216 + (i // 4) * 26
        b += f'<circle cx="{cx+5}" cy="{cy-4}" r="5" fill="{pal[i]}"/>' + T(t, cx + 18, cy, f"{n}  {v*100/tot:.0f}%", 12, t["text"], FM)
    return svg(t, 1000, 268, b)

if __name__ == "__main__":
    nums, langs = fetch()
    for tn, t in THEMES.items(): write("stats", tn, build(t, nums, langs))
    print("wrote assets/stats-dark.svg + stats-light.svg")
