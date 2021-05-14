import pandas as pd
import sqlite3 as sql


#######ecole
data = pd.read_excel('listeEcoles.xlsx', header=0)
database = sql.connect("concours.db")
c = database.cursor()

for i in range(len(data)): 
    nom = data['name'][i]
    code = int(data['code'][i])
    

    c.execute("INSERT INTO ecole VALUES (?,?)", (code,nom))
    database.commit()

#######etat_reponse
data = pd.read_excel('listeEtatsReponsesAppel.xlsx', header=0)


for i in range(len(data)):
    code = int(data['Ata _cod'][i])
    etat = data['Ata _lib'][i]
    

    c.execute("INSERT INTO etat_reponse VALUES (?,?)", (code,etat))
    database.commit()

#######etablissement
data = pd.read_excel('listeEtablissements.xlsx', header=0)


for i in range(len(data)):
    rne = data['rne'][i]
    type = data['type'][i]
    name = data['name'][i]
    cp = str(data['cp'][i])
    ville = data['ville'][i]
    pays = data['pays'][i]

    c.execute("INSERT INTO etablissement VALUES (?,?,?,?,?,?)", (rne,type,name,cp,ville,pays))
    database.commit()


#######csp_parent
data = pd.read_excel('Inscription.xlsx', header=1)
L = []

for i in range(len(data)):
    code = int(data['COD_CSP_PERE'][i])
    lib = data['LIB_CSP_PERE'][i]
    
    if code not in L :
        L.append(code)
        c.execute("INSERT INTO csp_parent VALUES (?,?)", (code,lib))
        database.commit()
for i in range(len(data)):
    code = int(data['COD_CSP_MERE'][i])
    lib = data['LIB_CSP_MERE'][i]
    
    if code not in L :
        L.append(code)
        c.execute("INSERT INTO csp_parent VALUES (?,?)", (code,lib))
        database.commit()

##########pays
L = []
for i in range(len(data)):
    code = int(data['CODE_PAYS_NAISSANCE'][i])
    pays = data['PAYS_NAISSANCE'][i]
    if code not in L :
        L.append(code)
        c.execute("INSERT INTO pays VALUES (?,?)", (code,pays))
        database.commit()
for i in range(len(data)):
    code = int(data['CODE_PAYS_NATIONALITE'][i])
    pays = data['AUTRE_NATIONALITE'][i]
    if code not in L :
        L.append(code)
        c.execute("INSERT INTO pays VALUES (?,?)", (code,pays))
        database.commit()
