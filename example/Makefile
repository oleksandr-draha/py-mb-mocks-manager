DOCKER_COMPOSE := $(shell command -v docker-compose >/dev/null 2>&1 && echo "docker-compose" || echo "docker compose")
SRC_FOLDERS = apps tests

.PHONY: start
start:
	$(DOCKER_COMPOSE) up

.PHONY: test
test:
	$(DOCKER_COMPOSE) run tests && $(DOCKER_COMPOSE) stop

.PHONY: lint
lint:
	poetry run black $(SRC_FOLDERS)

.PHONY: sort-imports
sort-imports:
	isort $(SRC_FOLDERS)

.PHONY: flake
flake:
	flake8 $(SRC_FOLDERS) --ignore=E501
