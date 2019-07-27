run:
	mkdocs serve --dev-addr=0.0.0.0:8080

deploy:
	mkdocs gh-deploy

test:
	python3 setup.py test

coverage:
	coverage run --source=src setup.py test
	coverage report
	coverage html

lint:
	pycodestyle .
