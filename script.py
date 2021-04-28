import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel('listeEcoles.xlsx')
dt = pd.read_excel('listeEtablissements.xlsx')


engine = create_engine('sqlite:///mydata.db')

df.to_sql('ecole', con=engine, if_exists='replace',index=False,index_label=None)
dt.to_sql('etablissement', con=engine, if_exists='replace',index=False,index_label=None)



