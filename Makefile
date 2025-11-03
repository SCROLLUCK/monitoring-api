.PHONY: run test test-cov test-fast test-report clean

run:
	poetry run python -m src.main

test:
	poetry run pytest -v --disable-warnings 


test-cov:
	poetry run pytest --cov=src --cov-report=html --cov-report=term-missing -v --disable-warnings

clean:
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf reports
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete