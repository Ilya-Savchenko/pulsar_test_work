run: migrate
	python3 project/manage.py runserver

migrate:
	python3 project/manage.py migrate

admin:
	python3 project/manage.py createsuperuser

models_to_csv:
	python3 project/manage.py models_to_csv

csv_to_models:
	python3 project/manage.py csv_to_models

