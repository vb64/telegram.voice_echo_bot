.PHONY: all run upload messages media lint flake8
ifeq ($(OS),Windows_NT)
PYTHONEXE = python.exe
PYTHON = venv\Scripts\$(PYTHONEXE)
else
PYTHONEXE = python
PYTHON = ./venv/bin/$(PYTHONEXE)
endif

S = source

all: run

run:
	$(PYTHON) $(S)/voice_echo.py

flake8:
	$(PYTHON) -m flake8 --max-line-length=110 $(S)

lint:
	$(PYTHON) -m pylint $(S)

setup: setup_python setup_pip

setup_pip:
	$(PYTHON) -m pip install -r requirements.txt

setup_python:
	python -m virtualenv venv
