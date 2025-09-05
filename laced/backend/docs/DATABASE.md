# Database Schema & Migrations for Laced

## Tables
- **users** — stores user data and hashed passwords
- **images** — uploaded/generated images and metadata
- **lora_models** — stores LoRA model training metadata
- **jobs** — scheduled and background tasks

## Relationships
- Users ↔ Images (one-to-many)
- Users ↔ LoRA models (one-to-many)

## Migrations
- Managed with Alembic
- Migration files located in `alembic/versions/`
- Ensure migrations are applied before running the backend
