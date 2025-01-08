FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    netcat-openbsd \
    iputils-ping \
    dnsutils \
    htop \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /example

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=/root/.local/bin:${PATH}
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-root && poetry cache clear -n --no-interaction pypi --all

COPY . .
