build:
	docker build -f docker/Dockerfile -t autocomplete_service .

start:
	@read -p "Rentrez le port sur lequel l'application doit tourner :" PORT;\
	docker run --rm -p $$PORT:$$PORT -e PORT=$$PORT -e HOSTNAME='0.0.0.0' -v logs:/app/logs autocomplete_service

cli:
	@read -p "Rentrez le port sur lequel l'application doit tourner :" PORT;\
	docker run --rm -p $$PORT:$$PORT -e PORT=$$PORT -e HOSTNAME='0.0.0.0' -v logs:/app/logs -ti --entrypoint /bin/sh autocomplete_service

start-local:
	cd src && python index.py

test:
	@read -p "Rentrez le port sur lequel l'application tourne :" PORT;\
	read -p "Rentrez le mot à compléter :" WORD;\
	echo "Réponse:\n";\
	curl http://localhost:$$PORT/autocomplete?query=$$WORD;\
	echo "\n"