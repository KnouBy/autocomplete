dev:
	@read -p "Rentrez le port sur lequel l'application doit tourner :" PORT;\
	docker run --rm --name autocomplete_app -p $$PORT:$$PORT -e PORT=$$PORT -e HOSTNAME='0.0.0.0' -v ${PWD}/logs:/app/logs -v ${PWD}/src:/app/src autocomplete_app

prod:
	docker run --rm --name autocomplete_app -p 8080:8080 -e PORT=8080 -e HOSTNAME='0.0.0.0' -v ${PWD}/logs:/app/logs autocomplete_app

build:
	@echo "Construction de l'image Docker"
	docker build -f docker/Dockerfile -t autocomplete_app .

cli:
	docker exec -ti autocomplete_app /bin/sh

start-local:
	cd src && python3.10 index.py

test:
	@read -p "Rentrez le port sur lequel l'application tourne :" PORT;\
	read -p "Rentrez le mot à compléter :" WORD;\
	echo "Réponse:\n";\
	curl http://localhost:$$PORT/autocomplete?query=$$WORD;\
	echo "\n"

pytest:
	cd src && pytest