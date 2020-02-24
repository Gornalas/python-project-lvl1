install: 
	poetry install
	poetry add prompt

lint:
	poetry run flake8 brain-games


.PHONY: install lint selfcheck check build
