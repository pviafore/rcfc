test: init
		py.test tests

init:
		pip install -r requirements.txt

.PHONY: init test