.DEFAULT_GOAL = help

install: env  ## Install dependencies with poetry
	poetry install --extras psycopg2-binary

env:  ## Create or copy example as .env
	test ! -f .env && cp .env.example .env || true

start:  ## Run bot
	poetry run python3 slack_bot/app.py

db-prepare:  ## Run DB in container and apply migrations
	docker compose run --rm bot make migrate && docker compose stop db

build:  ## Build all
	docker compose -f docker-compose.yml build

up:  ## Up all and show logs
	docker compose -f docker-compose.yml up -d && docker-compose -f docker-compose.yml logs -f --tail=10

update:  ## Restart bot after files changing
	docker compose -f docker-compose.yml restart bot && make up

stop:  ## Stop all
	docker compose -f docker-compose.yml stop

down:  ## Down all
	docker compose -f docker-compose.yml down

migration: ## Create migration
	poetry run alembic revision --autogenerate

migrate:  ## Apply migrations
	poetry run alembic upgrade head

lint:  ## Check lint
	poetry run flake8 slack_bot

help:  ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | sort \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[0;32m%-30s\033[0m %s\n", $$1, $$2}'
