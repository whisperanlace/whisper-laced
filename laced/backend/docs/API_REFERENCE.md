# API Reference

## Authentication
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive JWT token

## Users
- `GET /users/{id}` — Fetch user info
- `POST /users/` — Create user
- `PUT /users/{id}` — Update user
- `DELETE /users/{id}` — Delete user

## Images
- `POST /images/upload` — Upload image
- `GET /images/{id}` — Retrieve image
- `POST /images/process` — Apply processing (watermark, mirror, resize)

## LoRA
- `POST /lora/train` — Start LoRA training
- `GET /lora/{id}` — Get LoRA info

## Jobs
- Celery tasks are auto-discovered in `jobs/`
