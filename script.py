import pandas as pd
import sqlite3 as sql

df = pd.read_excel('listeEcoles.xlsx')
dt = pd.read_excel('listeEtablissements.xlsx')
db = sql.connect("data.db")



df.to_sql('ecole', db, if_exists='replace',index=False,index_label=None)
dt.to_sql('etablissement', db, if_exists='replace',index=False,index_label=None)


