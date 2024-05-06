SHELL := /bin/bash

make containers:
	sudo docker compose -f local.yml up -d --build