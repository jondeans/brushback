VENV = venv
PYTHON_VERSION = 3.11
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: check
check:
	ruff check src/ tests/
	ruff format --check src/ tests/

.PHONY: clean
clean:
	ruff clean
	rm -rf $(VENV)
	rm -rf *.egg-info

venv:
	python -m venv $(VENV)
	$(PIP) install -U pip

.PHONY: fix
fix:
	ruff src/ tests/
	ruff format src/ tests/

.PHONY: install
install: venv
	$(PIP) install -e .

.PHONY: install-dev
install-dev: venv
	$(PIP) install -e ".[dev]"

.PHONY: install-nb
install-nb: venv
	$(PIP) install -e ".[nb]"

.PHONY: test
test:
	$(PYTHON) -m pytest tests
