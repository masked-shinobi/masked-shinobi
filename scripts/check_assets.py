"""Run before pushing:  python scripts/check_assets.py  — flags README images that don't exist locally."""
import re, os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
md = open(os.path.join(root, "README.md"), encoding="utf-8").read()
refs = re.findall(r'(?:src|srcset)="([^"]+)"', md)
bad = [p for p in refs if not p.startswith("http") and not os.path.exists(os.path.join(root, p))]
print("missing local assets:", bad or "none"); print("external image URLs:", sum(p.startswith("http") for p in refs))
sys.exit(1 if bad else 0)
