# Projet PII - Groupe 9

## Folder
- ressources : contient des fichiers complémentaire, par exemple le schéma du modèle de données
- web : contient le code du web
- Projet PII GRP-09 : contient les documents sources du rapport

## Files

- schemadb.txt : Code du schema de la base de donnée pour dbdiagram.io
- createdb.sql : Fichier pour créer les tables sous SQLite3
- import_files.py : Script pour remplir la base de données à partir des fichiers .xlsx
- verif_data.py + config_verif_data.txt : Script pour vérifier la cohérence de la base de donnée avec les fichiers non utilisés (Ne fait que vérifier, ne fait pas de modification)
- config_verif_data.txt : Sert à configurer les fichiers
- setup.py : Initialise ou crée la base de données
- rapport_Projet_PII_GRP_09.pdf : le rapport de projet PII du groupe 9

## Importer les tableurs dans la base de donnée

### Environnement de travail

Le mieux est de travailler dans un environnement virtuel

Sur Windows
```bash
python -m venv venv
./venv/Scripts/activate
```
Ou sur linux
```bash
python -m venv env
source env/bin/activate
```

>Pour  désactiver l'environnement virtuel :  
> ```bash
> deactivate
> ```

### En mode ligne de commande (avec click)
L'intégration automatique utilise le module setuptools
```bash
pip install --editable .
```

La commande à utilisée est alors `importxl` qui possède les options
* `--help`/`-h` pour afficher l'aide
* `--init`/`-i` pour initialiser la base de donnée
* `--import`/`-I` pour importer les données dans la BD
* `--verif`/`-v` pour vérifier la cohérence des données

### En mode scripts python
Il faut installer les modules nécessaires
```bash
pip install openpyxl
pip install pandas
```
Créer la base de donnée avec sqlite3 (ou décommenter les lignes 489 à 491)
```bash
sqlite3 concours.db -init createdb.sql
```
Puis lancer les scripts en changeant au préalable les chemins d'accès aux différents fichiers directement dans les scripts
```bash
./import_files.py
./verif_data.py
```

## Application

### Installation de Flask
1. Ouvrir un terminal
2. $ pip install flask

### Lancement du serveur Flask (sous Linux)
1. Ouvrir un terminal dans le répertoire /web
2. $ export FLASK_APP=app.py
3. $ export FLASK_DEBUG=1
4. $ flask run

### Lancement du serveur Flask (sous Window)
1. Ouvrir un terminal dans le répertoire /web
2. $ env:FLASK_APP = "app.py"
3. $ env:FLASK_DEBUG = 1
4. $ flask run

### Utilisation de l'application web
- http://127.0.0.1:5000/ : page d'accueil
- http://127.0.0.1:5000/rech : pour faire une recherche d'un candidat par son nom
- http://127.0.0.1:5000/candidatByCode/<candidat.code> : pour accéder directement aux informations d'un candidat par son numéro scei
- http://127.0.0.1:5000/voeux/<candidat.code> : pour afficher les voeux du candidat
- http://127.0.0.1:5000/notes/<candidat.code> : pour afficher les notes du candidat
- http://127.0.0.1:5000/classement/<candidat.code> : pour afficher le classement des candidats
- http://127.0.0.1:5000/ecole : pour afficher toutes les écoles
- http://127.0.0.1:5000/etablissement : pour afficher tous les établissements
- http://127.0.0.1:5000/epreuve : pour afficher toutes les épreuves
- http://127.0.0.1:5000/option : pour afficher tous les options
- http://127.0.0.1:5000/csp : pour afficher toutes les catégories socio-professionnelles
- http://127.0.0.1:5000/moyenne_forms : pour calculer la moyenne sur une épreuve pour un établissement, en fournissant le RNE de l'établissement
