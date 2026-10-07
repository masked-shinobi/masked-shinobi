"""Validate every local image referenced by README.md."""
import re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; md=(ROOT/'README.md').read_text(encoding='utf-8')
refs=re.findall(r'(?:src|srcset)="(\./assets/[^"?#]+)',md)
missing=[r for r in refs if not (ROOT/r[2:]).exists()]
print('README local assets:',len(refs)); print('missing:',missing or 'none'); sys.exit(1 if missing else 0)
