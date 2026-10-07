# Setup (2 minutes)
1. Create a **public** repo named exactly `masked-shinobi/masked-shinobi` and tick "Add a README" off.
2. Upload **everything** in this folder: `README.md`, `assets/`, `scripts/`, and the hidden `.github/` folder (use `git` or drag the folders in; hidden folders are skipped by some file pickers).
3. Repo → Settings → Actions → General → Workflow permissions → **Read and write**.
4. Actions tab → "Update profile assets" → **Run workflow**. This fills `stats.svg` and `github-snake.svg` with live data (it then refreshes every 12h).
5. Optional check before pushing: `python scripts/check_assets.py`
