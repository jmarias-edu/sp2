SHELL := /bin/bash

make rebuild:
	sudo docker compose -f local.yml up -d --build

make makemigrations:
	sudo docker compose -f local.yml run --rm django python manage.py makemigrations

make migrate:
	sudo docker compose -f local.yml run --rm django python manage.py migrate

make backlogs:
	sudo docker logs -f omgenes_local_django

make frontlogs:
	sudo docker logs -f omegenes_frontend_image

make datalogs:
	sudo docker logs -f omgenes_production_postgres