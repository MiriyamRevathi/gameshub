.PHONY: install test run cli build clean lint

install:
	pip install -r requirements.txt

test:
	pytest --cov=. tests/

run:
	python app.py

cli:
	python main.py

build:
	python -m compileall .

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
