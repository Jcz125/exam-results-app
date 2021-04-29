# Projet PII - Groupe 9

## Files

- schemadb.txt : Code du schema de la base de donnée pour dbdiagram.io
- createdb.sql : Fichier pour créer les tables sous SQLite3
- concours.db : Fichier database, notre base de données
- export.py : Script pour exporter les données depuis un fichier Excel .xlsx et les importer dans notre base de données concours.db
- Inscription.xlsx : Fichier Excel, celui-ci est trop gros, veuillez l'importer vous même dans votre dossier de travail (non mis sur le dépôt git)

## Environnement
Avant d'exécuter le fichier export.py vous devez avoir un environnement (de préférence) dans lequel vous avez les bibliothèques openpyxl, xlrd, pandas. 

Commandes pour avoir ces bibliothèques :

- Dans un environnement python (venv) :
    $ pip install nom_library

- Dans une console (Linux):
    $ sudo apt-get install python3-pip
    $ sudo -H pip3 install nom_library

Pour avoir python3 : sudo apt-get install python3

Pensez également à mettre à jour les modules :
$ sudo apt update
$ sudo apt upgrade
