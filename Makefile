install: 
	poetry install

lint:
	poetry run flake8 brain-games


.PHONY: install lint
