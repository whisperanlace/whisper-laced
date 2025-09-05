# Laced — Root README

This folder is the root for the Laced service inside the Whisper-Laced monorepo.
It contains production-ready runtime config, containerization assets, DB migration
config, and operational scripts. All backend and frontend code lives in the
`backend/` and `frontend/` directories respectively.

This root commit includes:
- runtime config: `laced_config.json`
- docker and compose assets
- database migration config (Alembic)
- operational scripts for seeding, backups, and model updates
- CI pipeline example and Kubernetes manifests

**This README intentionally avoids local-only dev instructions** — the codebase
is production-ready. See `backend/` for the API and `frontend/` for the UI.

## Quick file list (root)
See files listed in root. Use `.env.example` to populate required environment variables.

## License
MIT — see `LICENSE`.
