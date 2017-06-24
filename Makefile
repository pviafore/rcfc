test: pep8
		py.test tests

init:
		pip install -r requirements.txt
		pip install -r dev_requirements.txt

pep8: init
		pep8 rcfc tests

.PHONY: init test
