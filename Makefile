PYTHON := python3
VENV := .venv
VENV_PY := $(VENV)/bin/python

run:
	@if [ ! -d "$(VENV)" ]; then $(PYTHON) -m venv $(VENV); fi
	@$(VENV_PY) -m pip install -U pip
	@$(VENV_PY) -m pip install -r requirements.txt
	@$(VENV_PY) src/main.py
