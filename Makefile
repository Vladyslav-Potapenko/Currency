run:
	python app/manage.py runserver

migrate:
	python app/manage.py migrate

makemigrations:
	python app/manage.py makemigrations

shell:
	python app/manage.py shell_plus --print-sql

createsuperuser:
	python app/manage.py createsuperuser

worker:
	python app ; celery -A settings worker -l info -P solo

beat:
	cd app/ ; celery -A settings beat -l info

