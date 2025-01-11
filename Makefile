DOCKER_COMPOSE := $(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")
SRC_FOLDERS = mountebank_mocks_manager example

.PHONY: lint
lint:
	poetry run black $(SRC_FOLDERS)

.PHONY: sort-imports
sort-imports:
	isort $(SRC_FOLDERS)

.PHONY: flake
flake:
	flakeheaven lint $(SRC_FOLDERS)
