SHELL := /bin/bash

ssh:
	ssh -i /home/mirage/.ssh/omgenes_digital_ocean root@104.248.151.246

rsync:
	rsync -av -e "ssh -i /home/mirage/.ssh/omgenes_digital_ocean" --exclude 'omgenes/media' --exclude '.snakemake' omgenes root@104.248.151.246:/root

compose:
	sudo docker compose -f production.yml up -d --build

restart:
	sudo docker compose -f production.yml up -d