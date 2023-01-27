install: .env
	poetry install

.env:
	test ! -f .env && cp .env.example .env

start:
	poetry run python3 slack_bot/app.py

docker-build:
	docker build -t dailybot .

docker-start:
	docker run -ti --label dailybot dailybot make start

lint:
	poetry run flake8 slack_bot
