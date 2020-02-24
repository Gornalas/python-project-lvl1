install: 
	poetry install
	poetry add prompt
	poetry add wemake_python_styleguide

lint:
	poetry run flake8 brain_games.py
	poetry run flake8 cli.py

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install lint selfcheck check build
