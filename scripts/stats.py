"""Fetch live GitHub metrics and regenerate the metrics SVG."""
import os,json,urllib.request,datetime,collections
from gen import THEMES,svg,panel,T,write,USER,FM
def api(path):
 h={'Accept':'application/vnd.github+json','User-Agent':'profile-stats'}
 if os.getenv('GITHUB_TOKEN'): h['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
 return json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com'+path,headers=h),timeout=20))
def fetch():
 try:
  u=api(f'/users/{USER}'); repos=[r for r in api(f'/users/{USER}/repos?per_page=100&type=owner') if not r.get('fork')]
  return [(str(u.get('public_repos',0)),'PUBLIC REPOS'),(str(sum(r.get('stargazers_count',0) for r in repos)),'STARS EARNED'),(str(u.get('followers',0)),'FOLLOWERS'),(str(sum(r.get('forks_count',0) for r in repos)),'FORKS')]
 except Exception as e:
  print('GitHub API unavailable; fallback:',e); return [('18','PUBLIC REPOS'),('—','STARS EARNED'),('—','FOLLOWERS'),('—','FORKS')]
def build(t,nums):
 b=f'<rect width="1200" height="150" rx="18" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
 for i,(n,l) in enumerate(nums):
  x=24+i*294; b+=panel(t,x,16,270,118,False,14)+T(t,x+20,54,n,34,t['a'][i],w=850)+T(t,x+20,84,l,10.5,t['mut'],FM,700,ls=1.5)+f'<circle cx="{x+238}" cy="50" r="18" fill="{t["a"][i]}" opacity=".09"/><path d="M{x+231} 50l5 5 10-12" stroke="{t["a"][i]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
 b+=T(t,1172,132,'updated '+datetime.date.today().isoformat(),9.5,t['soft'],FM,600,'end')
 return svg(t,1200,150,b,'Live GitHub profile metrics')
if __name__=='__main__':
 nums=fetch()
 for th,t in THEMES.items(): write('metrics',th,build(t,nums))
 print('updated metrics')
