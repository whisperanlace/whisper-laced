.PHONY: help build up down migrate seed backup restore test lint

help:
	@echo "targets: build up down migrate seed backup restore test lint"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	alembic upgrade head

seed:
	./scripts/seed_admin.sh

backup:
	./scripts/backup_db.sh

restore:
	./scripts/restore_db.sh

test:
	pytest -q

lint:
	# Add linters as desired
	@echo "linting not configured"
