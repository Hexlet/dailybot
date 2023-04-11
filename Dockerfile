FROM python:3.10.4-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.2.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin" \
    POSTGRES_USER=${POSTGRES_USER} \
    POSTGRESS_PASSWORD=${POSTGRESS_PASSWORD} \
    POSTGRES_DB=${POSTGRES_DB} \
    POSTGRES_SERVER=${POSTGRES_SERVER}

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    curl \
    make \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY . /app/

RUN poetry install
