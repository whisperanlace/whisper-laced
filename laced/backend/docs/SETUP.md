# Local Development Setup for Laced

Prepare your local environment for development.

## Steps
1. Clone the repository
2. Create a virtual environment for Python
3. Install all dependencies from `requirements.txt`
4. Configure `.env` file with database, Redis, email, and secret keys
5. Apply database migrations
6. Start the backend server
7. Run tests to ensure everything works

## Notes
- Use separate `.env` files for development, staging, and production
- Make sure the logging directory exists and is writable
- All environment-specific settings are managed in `config/settings.py`
