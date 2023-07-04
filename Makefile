test:
	coverage run --source='./website' --omit='website/migrations/*' manage.py test && echo "\nCoverage\n" && coverage report

lint:
	-flake8 --exclude=migrations --max-line-length=120 .
	@echo "\n"
	-black --check --exclude /migrations/ .
