import pandas as pd
import sqlite3 as sql
import openpyxl as xl
from pathlib import Path


# liste_etat_dossier = []
# liste_concours = []
# liste_autres_prenoms = []
# liste_serie_bac = []

####### initialisation de la table ep_option pour 0/NULL/NULL
# liste_ep_option = []
# c.execute("INSERT INTO ep_option(id) VALUES (0);")
# database.commit()

# dictionnaires des épreuves
dico_epreuves = {

    ##### ECRITES #####
    "Langue": 28,
    "Informatique ou Sciences industrielles": 599,
    "Mathématiques 1": 600,
    "Mathématiques 2": 601,
    "Physique 1": 602,
    "Physique 2": 603,
    "Chimie": 604,
    "Français": 605,
    "Sciences industrielles": 606,
    "Informatique": 1050,
    "bonification_ecrit": 9898,
    "total_ecrit": 9899,

    ##### SPECIFIQUES CMT #####
    "QCM info/physique": 1,
    "Entretien nouvelles technologies": 2,
    "QCM anglais": 3,
    "Mathématiques spe CMT": 4,                 # ajout de spe CMT

    ##### ORALES CMT #####
    "Physique ou Sciences industrielles": 5,
    "Entretien": 6,
    "Anglais oral CMT": 7,                      # ajout de oral CMT
    "Mathématiques oral CMT": 8,                # ajout de oral CMT

    ##### ORALES CCMP #####
    "Physique": 9,
    "Français oral CCMP": 10,                   # ajout de oral CCMP
    "Anglais": 11,
    "Mathématiques": 12,

    ##### TOTAL ORAL #####
    "Mathématiques (harmonisé)": 400,
    "Mathématiques (affichée)":401,
    "max_physique": 9900,
    "max_anglais": 9901,
    "bonification_oral": 9998,
    "total_oral": 9999,

    ##### TOTAL (ECRIT+ORAL) ######
    "total": 10000,

    ##### CLASSEMENT #####
    "bonus_interclassement": 10198,
    "total_avec_interclassement": 10199,
    "note_entretien_exaequo": 10200,
    "note_anglais_exaequo": 10201,

    ##### ECRITES PT #####
    "Mathématiques B": 700,
    "Mathématiques C": 701,
    "Physique A": 702,
    "Physique B": 703,
    "Informatique modélisation": 704,
    "Sciences industrielles A": 705,
    "Français B": 706,
    "Langue A": 707,

    ##### ECRITES TSI #####
    "Mathématiques 1 TSI": 800,                 # ajout de TSI
    "Mathématiques 2 TSI": 801,                 # ajout de TSI
    "Physique 1 TSI": 802,                      # ajout de TSI
    "Physique 2 TSI": 803,                      # ajout de TSI
    "Français TSI": 804,                        # ajout de TSI
    "Langue TSI": 805,                          # ajout de TSI
    "Sciences industrielles TSI": 806,          # ajout de TSI
    "Informatique TSI": 807,                    # ajout de TSI

    ##### ORALES CCS #####
    "Mathématiques 1 oral TSI": 13,             # ajout de oral TSI
    "Mathématiques 2 oral TSI": 14,             # ajout de oral TSI
    "Physique-chimie 1 oral TSI": 15,           # ajout de oral TSI
    "Physique-chimie 2 oral TSI": 16,           # ajout de oral TSI
    "Langue vivante oral TSI": 17,              # ajout de oral TSI
    "TP Physique-chimie oral TSI": 18,          # ajout de oral TSI
    "S2I oral TSI": 19                          # ajout de oral TSI

}

liste_ep = [
    ##### ECRITES #####
    "Langue", #: 28,
    "Informatique ou Sciences industrielles", #: 599,
    "Mathématiques 1", #: 600,
    "Mathématiques 2", #: 601,
    "Physique 1", #: 602,
    "Physique 2", #: 603,
    "Chimie", #: 604,
    "Français", #: 605,
    "Sciences industrielles", #: 606,
    "Informatique", #: 1050,
    "bonification_ecrit", #: 9898,
    "total_ecrit", #: 9899,

    ##### SPECIFIQUES CMT #####
    "QCM info/physique", #: 1,
    "Entretien nouvelles technologies", #: 2,
    "QCM anglais", #: 3,
    "Mathématiques", #: 4,                 # ajout de spe CMT

    ##### ORALES CMT #####
    "Physique ou Sciences industrielles", #: 5,
    "Entretien", #: 6,
    "Anglais", #: 7,                      # ajout de oral CMT
    "Mathématiques", #: 8,                # ajout de oral CMT

    ##### ORALES CCMP #####
    "Physique", #: 9,
    "Français", #: 10,                   # ajout de oral CCMP
    "Anglais", #: 11,
    "Mathématiques", #: 12,

    ##### TOTAL ORAL #####
    "Mathématiques (harmonisé)", #: 400,
    "Mathématiques (affichée)", #:401,
    "max_physique", #: 9900,
    "max_anglais", #: 9901,
    "bonification_oral", #: 9998,
    "total_oral", #: 9999,

    ##### TOTAL (ECRIT+ORAL) ######
    "total", #: 10000,

    ##### CLASSEMENT #####
    "bonus_interclassement", #: 10198,
    "total_avec_interclassement", #: 10199,
    "note_entretien_exaequo", #: 10200,
    "note_anglais_exaequo", #: 10201,

    ##### ECRITES PT #####
    "Mathématiques B", #: 700,
    "Mathématiques C", #: 701,
    "Physique A", #: 702,
    "Physique B", #: 703,
    "Informatique modélisation", #: 704,
    "Sciences industrielles A", #: 705,
    "Français B", #: 706,
    "Langue A", #: 707,

    ##### ECRITES TSI #####
    "Mathématiques 1", #: 800,                 # ajout de TSI
    "Mathématiques 2", #: 801,                 # ajout de TSI
    "Physique 1", #: 802,                      # ajout de TSI
    "Physique 2", #: 803,                      # ajout de TSI
    "Français", #: 804,                        # ajout de TSI
    "Langue", #: 805,                          # ajout de TSI
    "Sciences industrielles", #: 806,          # ajout de TSI
    "Informatique", #: 807,                    # ajout de TSI

    ##### ORALES CCS #####
    "Mathématiques 1", #: 13,             # ajout de oral TSI
    "Mathématiques 2", #: 14,             # ajout de oral TSI
    "Physique-chimie 1", #: 15,           # ajout de oral TSI
    "Physique-chimie 2", #: 16,           # ajout de oral TSI
    "Langue vivante", #: 17,              # ajout de oral TSI
    "TP Physique-chimie", #: 18,          # ajout de oral TSI
    "S2I", #: 19                          # ajout de oral TSI
]

liste_cle_ep = [

    ##### ECRITES #####
    28,     # "Langue"
    599,    # "Informatique ou Sciences industrielles"
    600,    # "Mathématiques 1"
    601,    # "Mathématiques 2"
    602,    # "Physique 1"
    603,    # "Physique 2"
    604,    # "Chimie"
    605,    # "Français"
    606,    # "Sciences industrielles"
    1050,   # "Informatique"
    9898,   # "bonification_ecrit"
    9899,   # "total_ecrit"

##### SPECIFIQUES CMT #####
    1,      # "QCM info/physique"
    2,      # "Entretien nouvelles technologies"
    3,      # "QCM anglais"
    4,      # "Mathématiques spe CMT" # ajout de spe CMT

##### ORALES CMT #####
    5,      # "Physique ou Sciences industrielles"
    6,      # "Entretien"
    7,      # "Anglais oral CMT" # ajout de oral CMT
    8,      # "Mathématiques oral CMT" # ajout de oral CMT

##### ORALES CCMP #####
    9,      # "Physique"
    10,     # "Français oral CCMP" # ajout de oral CCMP
    11,     # "Anglais"
    12,     # "Mathématiques"

##### TOTAL ORAL #####
    400,    # "Mathématiques (harmonisé)"
    401,    # "Mathématiques (affichée)"
    9900,   # "max_physique"
    9901,   # "max_anglais"
    9998,   # "bonification_oral"
    9999,   # "total_oral"

##### TOTAL (ECRIT+ORAL) ######
    10000,  # "total"

##### CLASSEMENT #####
    10198,  # "bonus_interclassement"
    10199,  # "total_avec_interclassement"
    10200,  # "note_entretien_exaequo"
    10201,  # "note_anglais_exaequo"

##### ECRITES PT #####
    700,    # "Mathématiques B"
    701,    # "Mathématiques C"
    702,    # "Physique A"
    703,    # "Physique B"
    704,    # "Informatique modélisation"
    705,    # "Sciences industrielles A"
    706,    # "Français B"
    707,    # "Langue A"

##### ECRITES TSI #####
    800,    # "Mathématiques 1 TSI" # ajout de TSI
    801,    # "Mathématiques 2 TSI" # ajout de TSI
    802,    # "Physique 1 TSI" # ajout de TSI
    803,    # "Physique 2 TSI" # ajout de TSI
    804,    # "Français TSI" # ajout de TSI
    805,    # "Langue TSI" # ajout de TSI
    806,    # "Sciences industrielles TSI" # ajout de TSI
    807,    # "Informatique TSI" # ajout de TSI

##### ORALES CCS #####
    13,     # "Mathématiques 1 oral TSI" # ajout de oral TSI
    14,     # "Mathématiques 2 oral TSI" # ajout de oral TSI
    15,     # "Physique-chimie 1 oral TSI" # ajout de oral TSI
    16,     # "Physique-chimie 2 oral TSI" # ajout de oral TSI
    17,     # "Langue vivante oral TSI" # ajout de oral TSI
    18,     # "TP Physique-chimie oral TSI" # ajout de oral TSI
    19      # "S2I oral TSI" # ajout de oral TSI

]

liste_ecrits = [28, 599, 600, 601, 602, 603, 604, 605, 606, 1050, 9898, 9899, 700, 701, 702, 703, 704, 705, 706, 707,
                800, 801, 802, 803, 804, 805, 806, 807]
liste_oraux = [5, 6, 7, 8, 9, 10, 11, 12, 400, 401, 9900, 9901, 9998, 9999, 400, 401, 9900, 9901, 9998, 9999, 13, 14,
               15, 16, 17, 18, 19]
liste_specifique = [1, 2, 3, 4]
liste_classement = [10198, 10199, 10200, 10201]

liste_ep_MP = [28, 599, 600, 601, 602, 603, 604, 605, 1050, 9898, 9899, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 400, 401,
               9900, 9901, 9998, 9999, 10000, 10198, 10199, 10200, 10201]
liste_ep_PC = []
liste_ep_PSI = []
liste_ep_PT = []
liste_ep_TSI = []


########## REMPLISSAGE DE LA DB ##########

database = sql.connect("concours.db")
c = database.cursor()

# data = pd.read_excel('Inscription.xlsx', header=1)

"""
##### BOUCLE DANS LE FICHIER INSCRIPTION #####

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

    ####### ep_option
    for j in range(1, 5):
        ep, op = data[f'EPREUVE{j}'][i], data[f'OPTION{j}'][i]
        if ((type(ep) == str) or (type(op) == str)) & ([ep, op] not in liste_ep_option):
            liste_ep_option.append([ep, op])
            consigne_sql = "INSERT INTO ep_option(epreuve, option) VALUES (?, ?);"
            c.execute(consigne_sql, (ep, op))

data.close()

##### BOUCLE DANS LE DICO DES EPREUVES #####
for k in range(len(liste_ep)):

    ####### epreuve
    ep, cle = liste_ep[k], liste_cle_ep[k]
    type = float('nan')

    if cle in liste_ecrits:
        type = "ECRIT"
    elif cle in liste_oraux:
        type = "ORAL"
    elif cle in liste_specifique:
        type = "SPECIFIQUE"
    elif cle in liste_classement:
        type = "CLASSEMENT"

    consigne_sql = "INSERT INTO epreuve VALUES (?, ?, ?)"
    c.execute(consigne_sql, (cle, ep, type))

"""

##### BOUCLES POUR LES FICHIERS CLASSES #####
##### notes
try:
    file = xl.load_workbook(Path("Classes_MP_CMT_spe_XXXX.xlsx"), read_only=True)
    tab = file["Export Workbook"]

    rows = tab.rows
    next(rows)
    for line in rows:
        for k in range(13, 48):
            if line[k] != float('nan'):
                with c:
                    consigne_sql = "INSERT INTO notes VALUES(?, ?, ?)"
                    c.execute(consigne_sql, (line[0], liste_ep_MP[k], line[k]))
except sql.DatabaseError as e:
    print(e)
finally:
    file.close()
database.commit()
database.close()


""" Aides utiles
    file_path = 'D:\JCZ-Profil\Documents\Mes devoirs\1A Telecom Nancy\PPII\ppii2k21\dow\data\public\Inscription.xlsx'
    str_test = "insert into candidat(code, nom, date_de_naissance) values (?, ?, ?)"
    str = "INSERT INTO candidat(code, civilite, nom, prenom, date_de_naissance, classe, puissance, voie_concours, etablissement, adresse1, adresse2, code_postal, commune, code_adr_pays, mail, tel, por) VALUES (CODE_CANDIDAT, CIVILITE, nom, PRENOM, DATE_DE_NAISSANCE, CLASSE, PUISSANCE, VOIE, CODE_ETABLISSEMENT, ADRESSE1, ADRESSE2, CP, VILLE, CODE_PAYS, EMAIL, TELEPHONE, TEL_PORTABLE)"
    data = data.values()
"""
