SHELL := /bin/bash

ssh:
	ssh -i /home/mirage/.ssh/omgenes_digital_ocean root@104.248.151.246

rsync:
	rsync -av -e "ssh -i /home/mirage/.ssh/omgenes_digital_ocean" --exclude 'omgenes/media' --exclude '.snakemake' omgenes root@104.248.151.246:/root

rsync-make:
	rsync -av -e "ssh -i /home/mirage/.ssh/omgenes_digital_ocean" ./makefile root@104.248.151.246:/root

compose:
	sudo docker compose -f ./omgenes/production.yml up -d --build

restart:
	sudo docker compose -f ./omgenes/production.yml up -d

django-shell:
	sudo docker exec -it omgenes-django-1 /bin/bash