# SkillSync CI/CD Slice

A minimal slice of the SkillSync Job Board to demonstrate a full path:
**commit → lint/test → build → push image → deploy**.

## What this includes
- Flask app with `/health` and `/jobs`
- Pytest tests
- Flake8 linting
- Dockerfile
- GitHub Actions CI (`.github/workflows/ci.yml`) to lint, test, build, and push to GHCR
- GitHub Actions CD (`.github/workflows/cd.yml`) to deploy to Fly.io (optional)
- `docker-compose.yml` for local container run

## Local run
```bash
docker compose up --build
# open http://localhost:8000/health and http://localhost:8000/jobs
```

## CI (GitHub)
1. Create a new repo and push this folder.
2. On any push/PR, CI will lint, test, and push the Docker image to GHCR with the commit SHA tag.

## CD (Fly.io) – one-time setup
1. Install flyctl locally and run: `flyctl launch --no-deploy` (or rename `app` in fly.toml if taken).
2. Create and copy a Fly API token: `flyctl auth token`.
3. In your GitHub repo → Settings → Secrets and variables → Actions → **New repository secret**:
   - `FLY_API_TOKEN` = your token.
4. Push to `main`. The `CD` workflow will deploy.

## Voice‑over Recording Checklist (2–4 minutes)
- Show repo structure: `app/`, `tests/`, `Dockerfile`, `ci.yml`, `cd.yml`.
- Make a small code change (e.g., add a third job) and commit.
- Open **Actions** tab → show CI running (lint, tests, image push).
- Show **Packages** tab (GHCR) with the new image tag.
- Show **CD** run (Fly.io deploy) finishing green.
- Open the app URL → call `/health` and `/jobs` to verify.
- Explain how failures stop the pipeline (e.g., break a test to demo red build).

## Tech notes
- Flask 3.0, Python 3.12, Pytest, Flake8.
- Container listens on port 8000 (Gunicorn).