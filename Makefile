.PHONY: install test



default: test

install:
	@echo "Installing dependencies"
	@pip install -r requirements.txt

test:
	@echo "Running tests"
	@tox

build:
	@echo "Building package"
	@python -m build .

pip-install:
	@echo "Installing package"
	@pip install dist/*.whl

format:
	@echo "Formatting code"
	@tox -e format -- src tests

clean:
	@echo "Clean dist"
	@rm -rf dist

venv:
	@echo "Creating virtual environment"
	@python3 -m venv .venv
	@source .venv/bin/activate
	@pip install -r requirements.txt
	@pip install -e .

py-version:
	@asdf install python 3.10.12
	@asdf local python 3.10.12

