run:
	mkdocs serve --dev-addr=0.0.0.0:8080

deploy:
	mkdocs build --clean
	gulp deploy