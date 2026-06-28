# =====================================
# AI Business Intelligence Platform
# =====================================

.PHONY: install

install:
	pip install -r requirements.txt


.PHONY: run

run:
	uvicorn app.main:app --reload


.PHONY: docker-build

docker-build:
	docker compose build


.PHONY: docker-up

docker-up:
	docker compose up -d


.PHONY: docker-down

docker-down:
	docker compose down


.PHONY: docker-logs

docker-logs:
	docker compose logs -f


.PHONY: docker-restart

docker-restart:
	docker compose down
	docker compose up -d


.PHONY: format

format:
	black .


.PHONY: lint

lint:
	ruff check .


.PHONY: test

test:
	pytest


.PHONY: clean

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +