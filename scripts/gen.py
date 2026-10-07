"""Generates every themed SVG (dark + light) and README.md.
Usage:  python scripts/gen.py && python scripts/stats.py
Edit PROJECTS / CAPS / STACK below, re-run, push."""
import os
from html import escape as esc

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ASSETS = os.path.join(ROOT, "assets")
USER = "masked-shinobi"
FS = "-apple-system,'Segoe UI',Inter,Helvetica,Arial,sans-serif"
FM = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"

THEMES = {
    "dark":  dict(card="#151b23", stroke="#30363d", text="#e6edf3", mut="#8b949e", glow=".16",
                  a=["#8b7cff", "#22d3ee", "#f472b6", "#34d399"], extra=["#f59e0b", "#60a5fa", "#f87171", "#8b949e"]),
    "light": dict(card="#f6f8fa", stroke="#d0d7de", text="#1f2328", mut="#59636e", glow=".10",
                  a=["#6246ea", "#0e7490", "#be185d", "#047857"], extra=["#b45309", "#1d4ed8", "#b91c1c", "#6e7781"]),
}

CSS = """
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes cyc{0%{opacity:0}4%{opacity:1}30%{opacity:1}34%{opacity:0}100%{opacity:0}}
@keyframes dial{from{stroke-dashoffset:var(--c)}}
.pulse{animation:pulse 1.8s ease-in-out infinite}
.grow{transform-box:fill-box;transform-origin:left;animation:grow 1.4s ease-out both}
.cyc{opacity:0;animation:cyc 9s infinite}
.dial{animation:dial 1.8s ease-out both}
"""

# ---------------------------------------------------------------- data (edit me)
PROJECTS = [  # repo, title, tag, description (<=55 chars), tech
    ("AI-RESUME-ANALYSER", "AI Resume Analyser", "AI / NLP", "Scores resumes and returns actionable feedback", ["Python", "NLP"]),
    ("MinorProject_resembler", "Resembler", "AI / ML", "Similarity matching engine (minor project)", ["Python", "ML"]),
    ("MCQ_test_Maker_website", "MCQ Test Maker", "WEB APP", "Create, share and grade multiple-choice tests", ["JavaScript", "Web"]),
    ("devops_webapp_cloud", "DevOps Web App", "CLOUD", "Containerised app with a cloud delivery pipeline", ["Docker", "CI/CD"]),
    ("CyberSecurity_Web_Centinel", "Web Sentinel", "SECURITY", "Security monitoring interface for web apps", ["Security", "Web"]),
    ("GSAP-website-3d", "GSAP 3D Website", "FRONTEND", "Scroll-driven 3D motion landing page", ["GSAP", "3D"]),
    ("Food-delivery-app-reactnative", "Food Delivery App", "MOBILE", "Cross-platform ordering experience", ["React Native"]),
    ("Organ-Donation-Platform-BlockChain", "Organ Donation Platform", "BLOCKCHAIN", "Transparent donor matching on-chain", ["Solidity", "Web3"]),
    ("email-simulator-CN", "Email Simulator", "NETWORKS", "Mail-protocol simulation for networking study", ["Networks", "SMTP"]),
    ("DSA-C-with-gtest", "DSA in C++", "ALGORITHMS", "Data structures with GoogleTest coverage", ["C++", "gtest"]),
    ("file-manager-app", "File Manager", "APP", "Browse and organise files in one place", ["Kotlin"]),
    ("PTS-Algorithm", "PTS Algorithm", "ALGORITHMS", "Algorithm implementation and analysis", ["Algorithms"]),
]
CAPS = [  # title, tagline, tags
    ("Frontend", "Interfaces with intent", ["React", "GSAP", "Three.js", "CSS"]),
    ("Backend", "APIs and data layers", ["Node", "Python", "SQL"]),
    ("AI / RAG", "Retrieval pipelines", ["Embeddings", "LLMs", "Vector DB"]),
    ("Cloud & DevOps", "Ship it reliably", ["Docker", "CI/CD", "Cloud"]),
    ("Security", "Defensive tooling", ["Web Sec", "Monitoring", "Auth"]),
    ("Mobile & Algorithms", "Foundations that scale", ["React Native", "Kotlin", "DSA"]),
]
STACK = [
    ("LANGUAGES", ["Python", "JavaScript", "TypeScript", "C++", "Kotlin", "Solidity", "SQL"]),
    ("FRONTEND", ["React", "GSAP", "Three.js", "Tailwind", "HTML/CSS"]),
    ("BACKEND", ["Node.js", "Express", "REST", "PostgreSQL", "MongoDB"]),
    ("CLOUD / DEVOPS", ["Docker", "GitHub Actions", "CI/CD", "Linux"]),
    ("AI / DATA", ["RAG", "Embeddings", "Prompting", "scikit-learn"]),
    ("QUALITY", ["Unit tests", "gtest", "pytest", "Edge-case analysis"]),
]
GAUGES = [("FRONTEND", 92), ("BACKEND", 88), ("AI / RAG", 86), ("CLOUD", 82)]

# ---------------------------------------------------------------- helpers
def T(t, x, y, s, size=14, fill=None, font=FS, w=500, a="start", ls=0, op=1, cls="", st=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" '
            f'fill="{fill or t["text"]}" text-anchor="{a}" letter-spacing="{ls}" opacity="{op}" '
            f'class="{cls}" style="{st}">{esc(s)}</text>')

def svg(t, w, h, body):
    defs = "".join(f'<radialGradient id="g{i}" cx="0" cy="0" r="1"><stop offset="0" stop-color="{c}" '
                   f'stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
                   for i, c in enumerate(t["a"]))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img">'
            f'<defs>{defs}<style>{CSS}</style></defs>{body}</svg>')

def card(t, x, y, w, h, i=0, r=20):
    return (f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="{r}" fill="{t["card"]}" stroke="{t["stroke"]}"/>'
            f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="{r}" fill="url(#g{i%4})"/>')

def chips(t, x, y, items, color, maxw):
    s, cx = "", x
    for it in items:
        w = len(it) * 6.9 + 20
        if cx + w > x + maxw: break
        s += (f'<rect x="{cx:.0f}" y="{y}" width="{w:.0f}" height="24" rx="12" fill="{color}" fill-opacity=".12" '
              f'stroke="{color}" stroke-opacity=".45"/>' + T(t, cx + w / 2, y + 16, it, 11, color, FM, 600, "middle"))
        cx += w + 8
    return s

def write(name, theme, content):
    os.makedirs(ASSETS, exist_ok=True)
    with open(os.path.join(ASSETS, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f: f.write(content)

# ---------------------------------------------------------------- assets
def hero(t):
    a = t["a"]
    b = card(t, 0, 0, 640, 320, 0) + card(t, 660, 0, 340, 152, 1) + card(t, 660, 168, 166, 152, 2) + card(t, 834, 168, 166, 152, 3)
    b += f'<circle class="pulse" cx="48" cy="52" r="5" fill="{a[3]}"/>' + T(t, 62, 56, "BUILDING IN PUBLIC", 11, t["mut"], FM, 600, ls=2)
    b += T(t, 40, 126, "Sanjay Baskar", 56, w=800, ls=-1.5) + T(t, 42, 164, "DESIGN ENGINEER", 14, a[0], FM, 700, ls=4)
    for i, l in enumerate(["Creative interfaces meet serious engineering.",
                           "Frontend systems · Cloud · RAG pipelines.",
                           "Technology arranged so the result feels obvious."]):
        b += T(t, 42, 214, l, 18, t["mut"], cls="cyc", st=f"animation-delay:{i*3}s")
    b += chips(t, 40, 258, ["React", "Python", "Cloud", "RAG", "Security"], a[0], 560)
    b += T(t, 692, 44, "EDUCATION", 11, t["mut"], FM, 600, ls=2) + T(t, 692, 92, "SRM IST", 34, w=800)
    b += T(t, 692, 120, "B.Tech CSE · Chennai · Year 3", 13, t["mut"])
    b += T(t, 692, 236, str(len(PROJECTS)), 64, a[2], w=800) + T(t, 692, 280, "SELECTED BUILDS", 10.5, t["mut"], FM, 600, ls=1.5)
    b += T(t, 866, 236, "6", 64, a[3], w=800) + T(t, 866, 280, "DOMAINS", 10.5, t["mut"], FM, 600, ls=1.5)
    return svg(t, 1000, 320, b)

def cap(t, i, c):
    a, (title, tag, tags) = t["a"][i % 4], c
    b = card(t, 0, 0, 320, 168, i)
    b += T(t, 24, 38, f"{i+1:02d}", 12, a, FM, 700, ls=2) + f'<rect class="grow" x="56" y="33" width="36" height="3" rx="1.5" fill="{a}"/>'
    b += T(t, 24, 76, title, 21, w=800) + T(t, 24, 100, tag, 13, t["mut"]) + chips(t, 24, 122, tags, a, 276)
    return svg(t, 320, 168, b)

def project(t, i, p):
    a = t["a"][i % 4]; _, title, tag, desc, tech = p
    b = card(t, 0, 0, 480, 176, i)
    b += T(t, 452, 70, f"{i+1:02d}", 52, a, w=800, a="end", op=.2)
    b += T(t, 28, 44, tag, 11, a, FM, 700, ls=2) + T(t, 28, 78, title, 22, w=800) + T(t, 28, 104, desc, 13, t["mut"])
    b += chips(t, 28, 126, tech, a, 360) + T(t, 452, 150, "↗", 22, a, w=700, a="end")
    return svg(t, 480, 176, b)

def stack(t):
    h = len(STACK) * 54 + 20
    b = card(t, 0, 0, 1000, h, 1)
    for i, (lab, items) in enumerate(STACK):
        y = 24 + i * 54; a = t["a"][i % 4]
        b += T(t, 32, y + 17, lab, 11, t["mut"], FM, 700, ls=2) + chips(t, 200, y, items, a, 770)
        if i: b += f'<line x1="32" x2="968" y1="{y-15}" y2="{y-15}" stroke="{t["stroke"]}"/>'
    return svg(t, 1000, h, b)

def telemetry(t):
    b = card(t, 0, 0, 1000, 200, 3); C = 2 * 3.14159265 * 46
    for i, (lab, p) in enumerate(GAUGES):
        cx, cy, a = 125 + i * 250, 88, t["a"][i % 4]
        b += (f'<circle cx="{cx}" cy="{cy}" r="46" stroke="{t["stroke"]}" stroke-width="8"/>'
              f'<circle class="dial" cx="{cx}" cy="{cy}" r="46" stroke="{a}" stroke-width="8" stroke-linecap="round" '
              f'stroke-dasharray="{C:.2f}" stroke-dashoffset="{C*(1-p/100):.2f}" transform="rotate(-90 {cx} {cy})" style="--c:{C:.2f}"/>')
        b += T(t, cx, cy + 9, f"{p}%", 26, w=800, a="middle") + T(t, cx, 176, lab, 11, t["mut"], FM, 700, a="middle", ls=2)
    return svg(t, 1000, 200, b)

# ---------------------------------------------------------------- README
def pic(name, alt, w="100%"):
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{name}-dark.svg">'
            f'<img src="./assets/{name}-light.svg" width="{w}" alt="{alt}"></picture>')

def badge(label, logo, url):
    return f'<a href="{url}"><img src="https://img.shields.io/badge/{label}-6246ea?style=for-the-badge&logo={logo}&logoColor=white"/></a>'

def readme():
    P = pic
    proj = "".join(
        ("<tr>" if i % 2 == 0 else "") +
        f'<td width="50%"><a href="https://github.com/{USER}/{p[0]}">{P(f"project-{i+1:02d}", p[1])}</a></td>' +
        ("</tr>\n" if i % 2 else "") for i, p in enumerate(PROJECTS))
    caps = "".join(("<tr>" if i % 3 == 0 else "") + f'<td width="33%">{P(f"capability-{i+1:02d}", c[0])}</td>' +
                   ("</tr>\n" if i % 3 == 2 else "") for i, c in enumerate(CAPS))
    snake = f"https://raw.githubusercontent.com/{USER}/{USER}/output/github-snake"
    return f"""<div align="center">

{P("hero", "Sanjay Baskar — Design Engineer")}

<br/>

{badge("CODE", "github", f"https://github.com/{USER}")}
{badge("LINKEDIN", "linkedin", "https://www.linkedin.com/in/masked-shinobi-30a289377/")}
{badge("EMAIL", "gmail", "mailto:maskedprogrammer.in@gmail.com")}
{badge("RESUME", "googledrive", "https://drive.google.com/file/d/1QGokMLQhPTLxFkUjbR9Es9ofhuaZsnsl/view?usp=drive_link")}
{badge("LIVE_PORTFOLIO", "githubpages", f"https://{USER}.github.io/{USER}/")}

<br/>

<a href="#about"><b>About</b></a> &nbsp;·&nbsp; <a href="#capabilities"><b>Capabilities</b></a> &nbsp;·&nbsp; <a href="#projects"><b>Projects</b></a> &nbsp;·&nbsp; <a href="#stack"><b>Stack</b></a> &nbsp;·&nbsp; <a href="#activity"><b>Activity</b></a> &nbsp;·&nbsp; <a href="#contact"><b>Contact</b></a>

</div>

<br/>

{P("stats", "GitHub statistics")}

<br/>

## About

<table>
<tr>
<td width="62%" valign="top">

### Design engineer × builder

I build digital products where **creative interfaces meet serious engineering**.

My work spans frontend systems, cloud infrastructure, AI retrieval pipelines, security tooling, mobile apps and algorithmic foundations.

**The goal isn't more technology. It's technology arranged with enough intent that the result feels obvious.**

</td>
<td width="38%" valign="top">

```text
THINK  →  DESIGN  →  BUILD
  ↑                     ↓
LEARN  ←  SHIP    ←  TEST
```

`SRM IST · Chennai`  
`B.Tech CSE · Year 3`  
`Merit Scholarship`

</td>
</tr>
</table>

## Capabilities

<table>
{caps}</table>

## Projects

<table>
{proj}</table>

<details>
<summary><b>More from the lab &nbsp;↓</b></summary>

<br/>

| Build | Direction |
|---|---|
| RAG Architecture | Modular retrieval + prompt synthesis |
| Ecommerce Devin | AI-assisted e-commerce workflow |
| Tic Tac Toe Docker | Minimal container deployment |
| Python Unit Testing | Testing patterns + boundary analysis |
| SRM Placement Compass | DSA + interview preparation |

</details>

## Stack

{P("stack", "Technology stack")}

<br/>

{P("telemetry", "Skill telemetry")}

## How I work

<table>
<tr>
<td width="25%" valign="top"><b>01 · Think</b><br/>Architecture before implementation.</td>
<td width="25%" valign="top"><b>02 · Craft</b><br/>Interfaces with purpose.</td>
<td width="25%" valign="top"><b>03 · Verify</b><br/>Tests, edges, failure paths.</td>
<td width="25%" valign="top"><b>04 · Ship</b><br/>Small releases, real feedback.</td>
</tr>
</table>

<details>
<summary><b>Experience &nbsp;↓</b></summary>

<br/>

| | |
|---|---|
| **SRM IST** | B.Tech Computer Science Engineering · Chennai · Merit Scholarship |
| **King Faisal University** | AI / ML research: deep learning experimentation and applied intelligence |
| **CJ Network** | Web Engineering |
| **Infosys** | Python Development |

</details>

<details>
<summary><b>Current focus &nbsp;↓</b></summary>

<br/>

Cloud-native architecture · Retrieval-augmented generation · Developer experience · Cybersecurity interfaces · Algorithms + systems · Production-oriented testing

*make it work → make it understandable → make it worth using*

</details>

## Activity

<div align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="{snake}-dark.svg">
<img src="{snake}.svg" width="100%" alt="contribution snake">
</picture>
</div>

## Contact

<div align="center">

### Build something that deserves a system diagram.

{badge("EXPLORE_CODE", "github", f"https://github.com/{USER}")}
{badge("LINKEDIN", "linkedin", "https://www.linkedin.com/in/masked-shinobi-30a289377/")}
{badge("EMAIL", "gmail", "mailto:maskedprogrammer.in@gmail.com")}

<sub>SANJAY BASKAR · DESIGN ENGINEER · 2026</sub>

</div>
"""

def main():
    for tn, t in THEMES.items():
        write("hero", tn, hero(t)); write("stack", tn, stack(t)); write("telemetry", tn, telemetry(t))
        for i, c in enumerate(CAPS): write(f"capability-{i+1:02d}", tn, cap(t, i, c))
        for i, p in enumerate(PROJECTS): write(f"project-{i+1:02d}", tn, project(t, i, p))
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f: f.write(readme())
    print("generated assets + README.md")

if __name__ == "__main__":
    main()
