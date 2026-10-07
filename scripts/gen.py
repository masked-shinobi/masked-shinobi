"""Generate the complete GitHub profile visual system."""
from html import escape as esc
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; ASSETS=ROOT/'assets'; USER='masked-shinobi'
FS="-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Helvetica,Arial,sans-serif"; FM="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
THEMES={
'dark':dict(bg='#0a0d12',panel='#10151d',stroke='#252d38',text='#f5f7fa',mut='#8c98a8',soft='#667386',a=['#8b7cff','#22d3ee','#f472b6','#34d399'],grid='#1c2430',bar='#1b2330'),
'light':dict(bg='#f7f8fb',panel='#fff',stroke='#d9dee7',text='#141820',mut='#5f6978',soft='#7b8594',a=['#6246ea','#087f8f','#c02670','#07865b'],grid='#e7eaf0',bar='#e9edf3')}
PROJECTS=[
('AI-RESUME-ANALYSER','AI Resume Analyser','AI / NLP','Resume scoring + actionable feedback',['Python','NLP']),
('MinorProject_resembler','Resembler','AI / RAG','Similarity matching and retrieval',['Python','FAISS']),
('MCQ_test_Maker_website','MCQ Test Maker','WEB APP','Create, share and grade tests',['React','Supabase']),
('devops_webapp_cloud','DevOps Web App','CLOUD','Containerised delivery pipeline',['Docker','CI/CD']),
('CyberSecurity_Web_Centinel','Web Sentinel','SECURITY','Security monitoring interface',['Security','GSAP']),
('GSAP-website-3d','GSAP 3D Website','EXPERIENCE','Scroll-driven 3D motion system',['GSAP','Three.js']),
('Food-delivery-app-reactnative','Food Delivery App','MOBILE','Cross-platform ordering flow',['React Native','JS']),
('Organ-Donation-Platform-BlockChain','Organ Donation Platform','BLOCKCHAIN','Transparent donor matching on-chain',['Solidity','Ethereum']),
('email-simulator-CN','Email Simulator','NETWORKS','Protocol simulation for networking study',['Python','Sockets']),
('DSA-C-with-gtest','DSA in C++','ALGORITHMS','Data structures with test coverage',['C++','gtest']),
('file-manager-app','Android File Manager','ANDROID','Local file browsing and organisation',['Kotlin','Android']),
('PTS-Algorithm','PTS Algorithm','RESEARCH','Algorithm implementation and analysis',['C++','Python'])]
CAPS=[
('01','PRODUCT UI','Interfaces that feel engineered',['React','Next.js','GSAP','Three.js']),
('02','APPLICATIONS','APIs, services and data flows',['Node.js','Python','REST','Postgres']),
('03','AI / RAG','Retrieval systems with usable outputs',['LangChain','FAISS','Embeddings','LLMs']),
('04','CLOUD / DEVOPS','Build → test → ship with confidence',['Docker','Actions','Linux','GCP']),
('05','SECURITY','Defensive tooling and observability',['Web Sec','Auth','Monitoring','Threat UI']),
('06','FOUNDATIONS','Algorithms, mobile and quality',['C++','Kotlin','DSA','gtest'])]
STACK=[('LANGUAGES',['TypeScript','JavaScript','Python','C++','Java','Kotlin','Solidity']),('FRONTEND',['React','Next.js','GSAP','Three.js','Tailwind']),('BACKEND',['Node.js','Express','REST','PostgreSQL','Supabase']),('AI / DATA',['RAG','LangChain','FAISS','Embeddings','scikit-learn']),('CLOUD',['Docker','GCP','GitHub Actions','CI/CD','Linux']),('QUALITY',['Unit testing','gtest','pytest','TDD','Edge cases'])]
GAUGES=[('FRONTEND',92),('BACKEND',88),('AI / RAG',86),('CLOUD',82)]
CSS='''@keyframes blink{0%,100%{opacity:1}50%{opacity:.28}} @keyframes rise{from{transform:scaleY(.15);opacity:.2}to{transform:scaleY(1);opacity:1}} .blink{animation:blink 1.8s ease-in-out infinite}.rise{transform-box:fill-box;transform-origin:bottom;animation:rise 1.2s ease-out both}'''
def T(t,x,y,s,size=14,fill=None,font=FS,w=500,a='start',ls=0,op=1,cls='',style=''):
 return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" fill="{fill or t["text"]}" text-anchor="{a}" letter-spacing="{ls}" opacity="{op}" class="{cls}" style="{style}">{esc(str(s))}</text>'
def svg(t,w,h,body,aria):
 defs=''.join(f'<linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["a"][i%4]}" stop-opacity=".18"/><stop offset="1" stop-color="{t["a"][(i+1)%4]}" stop-opacity="0"/></linearGradient>' for i in range(4))
 defs+=f'<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>'
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img" aria-label="{esc(aria)}"><defs>{defs}<style>{CSS}</style></defs>{body}</svg>'
def panel(t,x,y,w,h,grad=True,r=18):
 s=f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="{r}" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
 return s+(f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="{r}" fill="url(#g{int(x+y)%4})"/>' if grad else '')
def pills(t,x,y,items,color,gap=8):
 s=''; cur=x
 for it in items:
  w=len(it)*6.8+22; s+=f'<rect x="{cur:.0f}" y="{y}" width="{w:.0f}" height="24" rx="12" fill="{color}" fill-opacity=".10" stroke="{color}" stroke-opacity=".38"/>'+T(t,cur+w/2,y+16,it,10.5,color,FM,650,'middle'); cur+=w+gap
 return s
def write(n,th,c): ASSETS.mkdir(exist_ok=True); (ASSETS/f'{n}-{th}.svg').write_text(c,encoding='utf-8')
def hero(t):
 a=t['a']; b=f'<rect width="1200" height="430" rx="24" fill="{t["bg"]}"/><rect width="1200" height="430" rx="24" fill="url(#grid)" opacity=".7"/><circle cx="940" cy="-30" r="270" fill="{a[0]}" opacity=".08"/><circle cx="1110" cy="410" r="230" fill="{a[1]}" opacity=".06"/>'
 b+=panel(t,24,24,744,382)+panel(t,788,24,388,182)+panel(t,788,222,388,184)
 b+=f'<circle class="blink" cx="58" cy="60" r="5" fill="{a[3]}"/>'+T(t,74,64,'AVAILABLE FOR BUILDING',11,t['mut'],FM,700,ls=2.4)+T(t,54,136,'Sanjay Baskar',60,w=850,ls=-2)+T(t,56,170,'DESIGN ENGINEER  /  CLOUD + SECURITY',12,a[0],FM,750,ls=2.5)+T(t,56,212,'Creative interfaces meet serious engineering.',20,w=650)+T(t,56,242,'I design, build and test digital products across',15,t['mut'])+T(t,56,264,'frontend systems, cloud infrastructure and AI/RAG.',15,t['mut'])
 b+=pills(t,56,304,['React','Python','Cloud','RAG','Security'],a[0])+f'<line x1="56" y1="366" x2="720" y2="366" stroke="{t["stroke"]}"/>'+T(t,56,391,'SRM IST · CHENNAI',10.5,t['soft'],FM,700,ls=1.8)+T(t,720,391,'B.TECH CSE · YEAR 3 · MERIT SCHOLARSHIP',10.5,t['soft'],FM,700,'end',1.3)
 b+=T(t,816,58,'SYSTEM STATUS',10.5,t['mut'],FM,700,ls=2)
 for i,(lab,val) in enumerate([('INTERFACE','CRAFTED'),('SERVICES','SHIPPABLE'),('PIPELINES','TESTED'),('EXPERIMENTS','ACTIVE')]):
  yy=92+i*25; col=a[i%4]; b+=f'<circle cx="820" cy="{yy-4}" r="4" fill="{col}"/>'+T(t,836,yy,lab,11,t['mut'],FM,650,ls=1)+T(t,1150,yy,val,11,col,FM,750,'end',1)
 b+=T(t,816,254,'BUILD SIGNAL',10.5,t['mut'],FM,700,ls=2)+T(t,816,292,'12',40,a[2],w=850)+T(t,882,292,'selected builds',11,t['mut'],FM,650)+T(t,816,338,'06',40,a[1],w=850)+T(t,882,338,'engineering domains',11,t['mut'],FM,650)+T(t,816,381,'make it work → make it clear → make it worth using',10,t['soft'],FM,600)
 return svg(t,1200,430,b,'Sanjay Baskar profile hero')
def metrics(t):
 nums=[('18','PUBLIC REPOS'),('—','STARS EARNED'),('—','FOLLOWERS'),('—','FORKS')]; b=f'<rect width="1200" height="150" rx="18" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
 for i,(n,l) in enumerate(nums):
  x=24+i*294; b+=panel(t,x,16,270,118,False,14)+T(t,x+20,54,n,34,t['a'][i],w=850)+T(t,x+20,84,l,10.5,t['mut'],FM,700,ls=1.5)+f'<circle cx="{x+238}" cy="50" r="18" fill="{t["a"][i]}" opacity=".09"/><path d="M{x+231} 50l5 5 10-12" stroke="{t["a"][i]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
 return svg(t,1200,150,b,'GitHub profile metrics')
def cap(t,i,c):
 num,title,tag,items=c; a=t['a'][i%4]; b=panel(t,0,0,380,192)+T(t,26,34,num,11,a,FM,800,ls=2)+T(t,354,34,'/ CAPABILITY',9.5,t['soft'],FM,650,'end',1.4)+T(t,26,74,title,19,w=800)+T(t,26,99,tag,12,t['mut'])+f'<rect x="26" y="120" width="326" height="1" fill="{t["stroke"]}"/>'+pills(t,26,140,items,a)
 return svg(t,380,192,b,title)
def project(t,i,p,wide=False):
 repo,title,tag,desc,tech=p; a=t['a'][i%4]; w=790 if wide else 580; h=230 if wide else 210; b=panel(t,0,0,w,h)+T(t,28,34,tag,10.5,a,FM,750,ls=2)+T(t,w-28,34,f'{i+1:02d}',11,t['soft'],FM,750,'end',2)+T(t,28,78,title,27 if wide else 22,w=850)+T(t,28,108,desc,13.5,t['mut'])+pills(t,28,136,tech,a)
 yy=h-50; b+=f'<line x1="28" y1="{yy}" x2="{w-28}" y2="{yy}" stroke="{t["stroke"]}"/>'+T(t,28,yy+26,'github.com/masked-shinobi/'+repo,9.5,t['soft'],FM,600)+T(t,w-28,yy+26,'OPEN PROJECT  ↗',10,a,FM,750,'end',1.2)
 for j in range(4):
  xx=w-170+j*35; b+=f'<circle cx="{xx}" cy="{yy-24}" r="4" fill="{t["a"][(i+j)%4]}"/>'+(f'<line x1="{xx+4}" y1="{yy-24}" x2="{xx+31}" y2="{yy-24}" stroke="{t["stroke"]}"/>' if j<3 else '')
 return svg(t,w,h,b,title)
def stack(t):
 b=panel(t,0,0,1200,360)
 for i,(lab,items) in enumerate(STACK):
  row=i//2; col=i%2; x=24+col*588; y=24+row*104; a=t['a'][i%4]; b+=panel(t,x,y,564,84,False,14)+T(t,x+18,y+22,lab,10.5,t['mut'],FM,750,ls=1.7)+pills(t,x+18,y+40,items,a)
 return svg(t,1200,360,b,'Technology stack')
def telemetry(t):
 b=panel(t,0,0,1200,230)+T(t,28,34,'ENGINEERING TELEMETRY',11,t['mut'],FM,750,ls=2.2)+T(t,1172,34,'SELF-ASSESSED SIGNAL',9.5,t['soft'],FM,650,'end',1.4)
 for i,(lab,p) in enumerate(GAUGES):
  y=72+i*37; a=t['a'][i]; b+=T(t,28,y+8,lab,11,t['text'],FM,700,ls=1.2)+f'<rect x="180" y="{y-4}" width="760" height="12" rx="6" fill="{t["bar"]}"/><rect class="rise" x="180" y="{y-4}" width="{760*p/100:.1f}" height="12" rx="6" fill="{a}"/>'+T(t,966,y+8,f'{p}%',12,a,FM,800,'end')+T(t,1172,y+8,['interface','services','retrieval','delivery'][i],10,t['soft'],FM,600,'end',1)
 return svg(t,1200,230,b,'Engineering telemetry')
def readme():
 def pic(n,a): return f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/{n}-dark.svg"><img src="./assets/{n}-light.svg" width="100%" alt="{esc(a)}"></picture>'
 def badge(l,logo,url): return f'<a href="{url}"><img src="https://img.shields.io/badge/{l}-6246EA?style=for-the-badge&logo={logo}&logoColor=white"></a>'
 caps=[]
 for k in range(0,6,3): caps.append('<tr>'+''.join(f'<td width="33%">{pic(f"capability-{i+1:02d}",CAPS[i][1])}</td>' for i in range(k,k+3))+'</tr>')
 rows=[f'<tr><td width="66%"><a href="https://github.com/{USER}/{PROJECTS[0][0]}">{pic("project-01",PROJECTS[0][1])}</a></td><td width="34%"><a href="https://github.com/{USER}/{PROJECTS[1][0]}">{pic("project-02",PROJECTS[1][1])}</a></td></tr>',f'<tr><td width="34%"><a href="https://github.com/{USER}/{PROJECTS[2][0]}">{pic("project-03",PROJECTS[2][1])}</a></td><td width="66%"><a href="https://github.com/{USER}/{PROJECTS[3][0]}">{pic("project-04",PROJECTS[3][1])}</a></td></tr>']
 for k in range(4,12,2): rows.append(f'<tr><td width="50%"><a href="https://github.com/{USER}/{PROJECTS[k][0]}">{pic(f"project-{k+1:02d}",PROJECTS[k][1])}</a></td><td width="50%"><a href="https://github.com/{USER}/{PROJECTS[k+1][0]}">{pic(f"project-{k+2:02d}",PROJECTS[k+1][1])}</a></td></tr>')
 lab=''.join(f'<tr><td><b>{p[1]}</b></td><td>{p[3]}</td><td><code>{" · ".join(p[4])}</code></td></tr>' for p in [PROJECTS[i] for i in [4,5,8,9,10,11]])
 exp='<tr><td><b>SRM IST</b></td><td>B.Tech Computer Science Engineering · Chennai · Merit Scholarship</td></tr><tr><td><b>King Faisal University</b></td><td>AI / ML research · deep learning experimentation and applied intelligence</td></tr><tr><td><b>CJ Network</b></td><td>Web Engineering</td></tr><tr><td><b>Infosys</b></td><td>Python Development</td></tr>'
 return f'''<div align="center">\n\n{pic('hero','Sanjay Baskar — Design Engineer')}\n\n<br/>\n\n{badge('CODE','github',f'https://github.com/{USER}')} {badge('LINKEDIN','linkedin','https://www.linkedin.com/in/masked-shinobi-30a289377/')} {badge('EMAIL','gmail','mailto:maskedprogrammer.in@gmail.com')} {badge('RESUME','googledrive','https://drive.google.com/file/d/1QGokMLQhPTLxFkUjbR9Es9ofhuaZsnsl/view?usp=drive_link')} {badge('LIVE_PORTFOLIO','githubpages','https://masked-shinobi.github.io/masked-shinobi/')}\n\n<br/><br/>\n\n<a href="#about"><b>ABOUT</b></a> · <a href="#capabilities"><b>CAPABILITIES</b></a> · <a href="#work"><b>WORK</b></a> · <a href="#stack"><b>STACK</b></a> · <a href="#activity"><b>ACTIVITY</b></a> · <a href="#contact"><b>CONTACT</b></a>\n\n</div>\n\n<br/>\n\n{pic('metrics','GitHub profile metrics')}\n\n<br/>\n\n## About · <sub>01</sub>\n\n<table><tr><td width="68%" valign="top">\n\n### Design engineer × builder\n\nI build digital products where **creative interfaces meet serious engineering**.\n\nMy work spans frontend systems, cloud infrastructure, AI retrieval pipelines, security tooling, mobile apps and algorithmic foundations.\n\n> **The goal isn't more technology. It's technology arranged with enough intent that the result feels obvious.**\n\n</td><td width="32%" valign="top">\n\n```text\nTHINK  →  DESIGN\n  ↑          ↓\nLEARN  ←  SHIP\n  ↑          ↓\nTEST   ←  BUILD\n```\n\n`SRM IST · Chennai`  \n`B.Tech CSE · Year 3`  \n`Merit Scholarship`\n\n</td></tr></table>\n\n## Capabilities · <sub>02</sub>\n\n<table>{''.join(caps)}</table>\n\n## Selected Work · <sub>03</sub>\n\n<table>{''.join(rows)}</table>\n\n<details><summary><b>LAB INDEX · more systems & experiments</b></summary>\n\n<br/>\n<table><tr><th>BUILD</th><th>DIRECTION</th><th>SIGNAL</th></tr>{lab}</table>\n</details>\n\n## Stack · <sub>04</sub>\n\n{pic('stack','Technology stack')}\n\n<br/>\n\n{pic('telemetry','Engineering telemetry')}\n\n## How I Work · <sub>05</sub>\n\n<table><tr><td width="25%"><b>01 / THINK</b><br/><sub>Architecture before implementation.</sub></td><td width="25%"><b>02 / CRAFT</b><br/><sub>Interfaces with purpose.</sub></td><td width="25%"><b>03 / VERIFY</b><br/><sub>Tests, edges, failure paths.</sub></td><td width="25%"><b>04 / SHIP</b><br/><sub>Small releases, real feedback.</sub></td></tr></table>\n\n<details><summary><b>EXPERIENCE · timeline</b></summary>\n\n<br/><table>{exp}</table>\n</details>\n\n<details><summary><b>CURRENT FOCUS · 2026</b></summary>\n\n<br/>`Cloud-native architecture` · `RAG systems` · `Developer experience` · `Cybersecurity interfaces` · `Algorithms + systems` · `Production testing`\n\n*make it work → make it understandable → make it worth using*\n\n</details>\n\n## Activity · <sub>06</sub>\n\n<div align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/github-snake-dark.svg"><img src="./assets/github-snake.svg" width="100%" alt="GitHub contribution snake"></picture></div>\n\n## Contact · <sub>07</sub>\n\n<div align="center">\n\n### Build something that deserves a system diagram.\n\n{badge('EXPLORE_CODE','github',f'https://github.com/{USER}')} {badge('LINKEDIN','linkedin','https://www.linkedin.com/in/masked-shinobi-30a289377/')} {badge('EMAIL','gmail','mailto:maskedprogrammer.in@gmail.com')}\n\n<br/>\n\n<sub>SANJAY BASKAR · DESIGN ENGINEER · 2026</sub>\n\n</div>\n'''
def main():
 for th,t in THEMES.items():
  write('hero',th,hero(t)); write('metrics',th,metrics(t)); write('stack',th,stack(t)); write('telemetry',th,telemetry(t))
  for i,c in enumerate(CAPS): write(f'capability-{i+1:02d}',th,cap(t,i,c))
  for i,p in enumerate(PROJECTS): write(f'project-{i+1:02d}',th,project(t,i,p,i in [0,3]))
 (ROOT/'README.md').write_text(readme(),encoding='utf-8'); print('generated README + assets')
if __name__=='__main__': main()
