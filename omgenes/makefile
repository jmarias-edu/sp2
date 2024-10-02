SHELL := /bin/bash

rebuild:
	sudo docker compose -f local.yml up -d --build

makemigrations:
	sudo docker compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	sudo docker compose -f local.yml run --rm django python manage.py migrate

backlogs:
	sudo docker logs -f omgenes_local_django

frontlogs:
	sudo docker logs -f frontend

datalogs:
	sudo docker logs -f omgenes_local_postgres

shell:
	sudo docker compose -f local.yml run --rm django python manage.py dbshell

start:
	sudo systemctl start docker

startbackend: start rebuild backlogs

prune:
	sudo docker system prune