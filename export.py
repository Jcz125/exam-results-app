import pandas as pd
import sqlite3 as sql


database = sql.connect("concours.db")
c = database.cursor()

data = pd.read_excel('Inscription.xlsx', header=1)
liste_etat_dossier = []
liste_concours = []
liste_autres_prenoms = []
liste_serie_bac = []

for i in range(len(data)):

    ####### etat_dossier
    code_etat_dossier = data['CODE_ETAT_DOSSIER'][i]
    lib_etat_dossier = data['LIBELLE_ETAT_DOSSIER'][i]
    if code_etat_dossier not in liste_etat_dossier:
        liste_etat_dossier.append(code_etat_dossier)
        consigne_sql = "INSERT INTO etat_dossier VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_etat_dossier), lib_etat_dossier))

    ####### concours
    code_concours = data['CODE_CONCOURS'][i]
    lib_concours = data['LIBELLE_CONCOURS'][i]
    voie_concours = data['VOIE'][i]
    if code_concours not in liste_concours:
        liste_concours.append(code_concours)
        consigne_sql = "INSERT INTO concours VALUES (?, ?, ?);"
        c.execute(consigne_sql, (int(code_concours), lib_concours, voie_concours))
    
    ####### autres_prenoms
    code_etudiant = data['CODE_CANDIDAT'][i]
    autre_prenom = data['AUTRES_PRENOMS'][i]
    couple = [code_etudiant, autre_prenom]
    if (type(autre_prenom) == str) & (couple not in liste_autres_prenoms):
        liste_autres_prenoms.append(couple)
        consigne_sql = "INSERT INTO autres_prenoms VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_etudiant), autre_prenom))
    
    ####### serie_bac
    code_serie = data['CODE_SERIE'][i]
    nom_serie = data['SERIE'][i]
    if code_serie not in liste_serie_bac:
        liste_serie_bac.append(code_serie)
        consigne_sql = "INSERT INTO serie_bac VALUES (?, ?);"
        c.execute(consigne_sql, (int(code_serie), nom_serie))


database.commit()
database.close()




""" Aides utiles
    file_path = 'D:\JCZ-Profil\Documents\Mes devoirs\1A Telecom Nancy\PPII\ppii2k21\dow\data\public\Inscription.xlsx'
    str_test = "insert into candidat(code, nom, date_de_naissance) values (?, ?, ?)"
    str = "INSERT INTO candidat(code, civilite, nom, prenom, date_de_naissance, classe, puissance, voie_concours, etablissement, adresse1, adresse2, code_postal, commune, code_adr_pays, mail, tel, por) VALUES (CODE_CANDIDAT, CIVILITE, nom, PRENOM, DATE_DE_NAISSANCE, CLASSE, PUISSANCE, VOIE, CODE_ETABLISSEMENT, ADRESSE1, ADRESSE2, CP, VILLE, CODE_PAYS, EMAIL, TELEPHONE, TEL_PORTABLE)"
    data = data.values()
"""