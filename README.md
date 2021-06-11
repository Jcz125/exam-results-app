# Projet PII - Groupe 9

## Folder
- /ressources : contient des fichiers complémentaire, par exemple le schéma du modèle de données
- /web : contient le code du web
- /Projet PII GRP-09 : contient les documents sources du rapport

## Files

- schemadb.txt : Code du schema de la base de donnée pour dbdiagram.io
- createdb.sql : Fichier pour créer les tables sous SQLite3
- import_files.py : Script pour remplir la base de données à partir des fichiers .xlsx
- verif_data.py + config_verif_data.txt : Script pour vérifier la cohérence de la base de donnée avec les fichiers non utilisés (Ne fait que vérifier, ne fait pas de modification)

## Importer les tableurs dans la base de donnée

### Environnement de travail

Le mieux est de travailler dans un environnement virtuel  
```bash
python -m pip virtualenv venv
./venv/Scripts/activate
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
