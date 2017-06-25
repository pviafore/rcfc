# Save off scripts as variables so that users can override them
# in the case of different python installations
PIP?=pip3
PYTHON?=python3
PYTEST?=py.test
PEP8?=pep8

test: pep8
		$(PYTEST) -v tests

init:
		$(PIP) install -r requirements.txt
		$(PIP) install -r dev_requirements.txt

pep8: init
		$(PEP8) rcfc tests

demo:
		cd rcfc && $(PYTHON) demo.py

.PHONY: init test pep8 demo
