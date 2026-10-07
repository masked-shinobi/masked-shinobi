# Single-repository setup

This version removes the old private-builder → public-profile split.

Use this as the root of `masked-shinobi/masked-shinobi`.

- `README.md` — profile UI
- `assets/` — local light/dark SVG visuals + contribution snake
- `scripts/gen.py` — content + SVG generator
- `scripts/stats.py` — live GitHub metrics
- `scripts/check_assets.py` — validation
- `.github/workflows/update-profile.yml` — automatic refresh every 12 hours

## Setup

1. Replace the contents of your profile repository with this folder.
2. Push to `main`.
3. Run **Actions → Refresh profile visuals → Run workflow** once.
4. Future runs refresh stats and the contribution snake automatically.

No second repo, PAT, hidden output branch, or README-copying step is required.

## Edit

Change `PROJECTS`, `CAPS`, `STACK`, and `GAUGES` in `scripts/gen.py`, then run:

```bash
python scripts/gen.py
python scripts/stats.py
python scripts/check_assets.py
```

The README uses only local `./assets/...` references, so the whole profile is self-contained.
