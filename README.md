# Exercice Autocomplete

# [Enoncé](ex001_autocomplete.pdf)

# Environnement de développement
- Python >3.10 ou Docker
- Linux
- make

# Comment utiliser l'application en developpement ?
## Avec Docker
Faire les étapes suivantes : 
```
make build
make dev
```
Insérer le port désiré pour faire tourner l'application.

## Avec Python directement
```
make start-local
```

## Tester
Vérifiez que l'application est bien lancée en local. Puis rentrez la commande :
```
make test
```
Insérez le port sur lequel l'application tourne puis le mot que vous souhaitez compléter.

# Comment faire tourner l'application en production ?
```
make build
make prod
```

# Structure de fichiers

data : Contient les fichiers de données d'exemple pour la base de données 
docker : Contient les fichiers nécessaires à la configuration de Docker
src : Contient le code source de l'application
