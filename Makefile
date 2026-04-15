PACKAGE_NAME = mazegen

install:
	pip install flake8 mypy build
run:
	python3 a_maze_ing.py config.txt

build:
	python3 -m pip install --upgrade build
	rm -rf dist/ build/ *.egg-info
	python3 -m build
	cp dist/*.whl .
	cp dist/*.tar.gz .
	rm -rf dist/ build/ *.egg-info

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	rm -rf dist/ build/ *.egg-info



lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict