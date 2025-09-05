# Deployment Guide for Laced Backend

This document provides complete production deployment instructions for the Laced backend with Whisper integration.

---

## Prerequisites

- Python 3.11+ installed
- PostgreSQL database ready
- Redis instance ready
- Docker & Docker Compose (optional but recommended)
- `.env` file with all secrets (database URL, Redis URL, email credentials, JWT secret key)

---

## Step 1: Clone the Repository

Clone the Laced repository to your server or deployment environment:

```bash
git clone <repository_url> laced-backend
cd laced-backend