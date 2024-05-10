SHELL := /bin/bash

make rebuild:
	sudo docker compose -f local.yml up -d --build

make makemigrations:
	sudo docker compose -f local.yml run --rm django python manage.py makemigrations

make migrate:
	sudo docker compose -f local.yml run --rm django python manage.py migrate