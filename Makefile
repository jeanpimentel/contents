all:

test: deps clean unit functional

deps:
	@pip install -q -r requirements-dev.txt

clean:
	@echo "Cleaning..."
	@find . -name '*.py[cod]' -delete
	@find . -name '.coverage' -delete

unit: clean
	@echo "Running unit tests..."
	@nosetests --with-coverage --cover-erase --cover-package=contents --stop --verbose --nocapture tests/unit

functional: clean
	@echo "Running functional tests..."
	@nosetests --stop --verbose --nocapture tests/functional

smell: clean
	@echo "Smelling code..."
	@echo "\n- PEP 8"
	@-pep8 contents
	@echo "\n- Pylint"
	@-pylint --output-format=parseable --reports=n --include-ids=y --disable=C0103,C0111 contents
