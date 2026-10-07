"""Run before pushing:  python scripts/check_assets.py  — flags any README image that doesn't exist locally."""
import re, os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
md = open(os.path.join(root, "README.md"), encoding="utf-8").read()
bad = [p for p in re.findall(r'src="([^"]+)"', md) if not p.startswith("http") and not os.path.exists(os.path.join(root, p))]
ext = [p for p in re.findall(r'src="(http[^"]+)"', md)]
print("missing local assets:", bad or "none"); print("external image URLs:", len(ext))
sys.exit(1 if bad else 0)
