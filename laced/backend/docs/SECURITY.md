# Security Guidelines for Laced

## Authentication
- JWT-based authentication using HS256
- Passwords hashed securely with bcrypt

## Middleware
- CORS configured for allowed domains
- Extendable for CSRF protection and rate-limiting

## Secrets Management
- All secrets stored in `.env` file
- Never commit secrets to version control

## Logging
- Logs are sanitized and do not store sensitive information
- Centralized logging via `config/logging_config.py`
