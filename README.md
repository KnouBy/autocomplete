# Exercice Autocomplete

# [Enoncé](ex001_autocomplete.pdf)

# Environnement de développement
- Python >3.10 ou Docker
- Linux
- make

# Comment utiliser l'application en développement ?
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

# Structure de fichiers
- data : Contient les fichiers de données d'exemple pour la base de données 
- docker : Contient les fichiers nécessaires à la configuration de Docker
- src : Contient le code source de l'application

# Changer de liste de mots
La liste utilisée est dans data/word_list.txt. Si vous désirez changer de liste, vous pouvez modifier ce fichier ou bien changer le path de la variable WORD_LIST_FILE dans le fichier search_database_provider.py.

# Pour aller plus loin
Ce système a été conçu très simplement. La base de données utilise la structure en Trie souvent utilisée pour les recherches rapides.

## Comment améliorer la pertinence des suggestions faites ?
### Séparation de mots
Ici pour des raisons de simplicité les mots séparés par un espace sont indexés comme 1 seul mot. On aurait pu indexer séparément les mots qui contiennent un ou plusieurs espaces comme plusieurs mots.
### Caractères spéciaux
Ici la gestion des caractères spéciaux n'a pas été traitée. 
- On ne simplifie pas les mots accentués en indexant dans la base de données. Cela signifie que si l'utilisateur recherche un mot qui contient un accent, il ne pourra pas le rechercher avec sa version non accentuée ("émission" ne sera pas retourné avec le préfix "em").
- On ne traite pas encore les mots de langues n'utilisant pas les caractères.
### Faute de frappe
On peut se dire qu'il arrive que l'utilisateur fasse une faute de frappe avant de faire sa recherche. Si aucun résultat n'est remonté de sa recherche, on peut alors essayer de faire des recherches "à une lettre près".

## Comment gérer un dictionnaire de termes de taille plus conséquente ?
### N'indexer que l'essentiel
D'après la consigne, on ne devrait retourner que les 4 premiers resultats de mots, les plus proches dans l'alphabet. Cela signifie que lorsque l'on indexe un mot dans la base de données, on peut se contenter de n'ajouter dans la liste des mots uniquement les 4 mots les plus hauts dans l'alphabet. Cela permettra de limiter l'espace mémoire nécessaire pour la recherche.
### Diminuer la mémoire
Pour le moment, chaque noeud contient la liste des mots qui correspondent à la recherche afin de ne pas parcourir l'ensemble de l'arbre.
Lorsque le dictionnaire deviendra beaucoup plus volumineux, cette structure deviendra trop lourde à charger en mémoire.
L'on pourra alors supprimer la liste des mots dans chaque noeud et reparcourir tout l'arbre jusqu'aux derniers noeuds. Cela ralentira un peu lors de la recherche.
### L'effort partagé
Sur de gros volumes de données, on pourra décider de répartir le service sur plusieurs machines pour aller plus vite lors de la recherche en parallélisant. Pour ceci on séparera la base de données en plusieurs, chaque partie sera indexée sur chaque machine. La recherche se fera en parallèle sur chaque machine et un reducer pourra faire la synthèse de toutes les recherches.

# Références
- [You autocomplete me](https://zepworks.com/posts/you-autocomplete-me/)
- [Wikipédia](https://fr.wikipedia.org/wiki/Trie_(informatique))

# Alternative de librairie d'autocomplétion
[fast-autocomplete](https://github.com/seperman/fast-autocomplete)