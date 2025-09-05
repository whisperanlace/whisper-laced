# Architecture Overview

## Folder Structure
app/
models/
routes/
services/
controllers/
schemas/
middleware/
jobs/
utils/
config/
tests/
docs/
frontend_helpers/

markdown
Copy code

## Key Components
- **Controllers**: Handle requests, responses, validation
- **Services**: Business logic, model interactions
- **Schemas**: Pydantic models for validation
- **Middleware**: Security, logging, rate limiting
- **Jobs**: Background and scheduled tasks (Celery)
- **Utils**: Reusable helpers (crypto, file, image, LoRA)
- **Config**: Environment, database, Celery, Redis, logging