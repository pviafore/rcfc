# Save off scripts as variables so that users can override them
# in the case of different python installations
PIP?=pip3
PYTHON?=python3
PYTEST?=py.test
PEP8?=pycodestyle

test: pep8
		PYTHONPATH=. $(PYTEST) -vvs tests

init:
		$(PIP) install -r requirements.txt
		$(PIP) install -r dev_requirements.txt

pep8: init
		$(PEP8) rcfc tests

demo:
		PYTHONPATH=. $(PYTHON) rcfc/demo.py

.PHONY: init test pep8 demo
