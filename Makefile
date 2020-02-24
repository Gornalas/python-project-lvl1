install: 
	poetry install
	poetry add prompt

lint:
	poetry run flake8 brain-games

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install lint selfcheck check build
