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
	sudo docker logs -f frontend

make datalogs:
	sudo docker logs -f omgenes_local_postgres

make shell:
	sudo docker compose -f local.yml run --rm django python manage.py dbshell

make start:
	sudo systemctl start docker

make startbackend: start rebuild backlogs