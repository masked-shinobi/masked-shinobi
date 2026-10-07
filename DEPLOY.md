# Profile v3 — deploy

1. Copy everything into the root of your `masked-shinobi/masked-shinobi` repo (keep `.github/`).
2. `python scripts/gen.py && python scripts/stats.py && python scripts/check_assets.py`
3. Push. The workflow refreshes stats every 12h and builds the contribution snake (`output` branch).
4. Settings → Pages → deploy from `main` / `/docs` for the interactive portfolio.

Edit `PROJECTS`, `CAPS`, `STACK`, `GAUGES` at the top of `scripts/gen.py` to change content.
Dark/light: every asset has `-dark` and `-light` versions; the README `<picture>` tags follow GitHub's theme.
