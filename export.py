import pandas as pd
import sqlite3 as sql

data = pd.read_excel('Inscription.xlsx', header=1)
# print(data['NOM']) # pour verifier le contenu
database = sql.connect("concours.db")

for i in range(len(data)): # exemple
    nom = data['NOM'][i]
    code = data['CODE_CANDIDAT'][i]
    
    # pas encore fini, à remplir suivant votre fonction

    # str_test = "insert into candidat(code, nom, date_de_naissance) values (?, ?, ?)"
    # str = "INSERT INTO candidat(code, civilite, nom, prenom, date_de_naissance, classe, puissance, voie_concours, etablissement, adresse1, adresse2, code_postal, commune, code_adr_pays, mail, tel, por) VALUES (CODE_CANDIDAT, CIVILITE, nom, PRENOM, DATE_DE_NAISSANCE, CLASSE, PUISSANCE, VOIE, CODE_ETABLISSEMENT, ADRESSE1, ADRESSE2, CP, VILLE, CODE_PAYS, EMAIL, TELEPHONE, TEL_PORTABLE)"
    # c.execute(str)


    # file_path = 'D:\JCZ-Profil\Documents\Mes devoirs\1A Telecom Nancy\PPII\ppii2k21\dow\data\public\Inscription.xlsx'