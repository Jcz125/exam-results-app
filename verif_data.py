from pathlib import Path
import pandas as pd
import openpyxl as xl
import sqlite3 as sql


def script(database: sql.Connection, path: Path):
    c = database.cursor()
    with open(Path('headers.txt'), 'r') as file:
        for line in file:
            if line[0] == '\t':
                ldata = line[1:-1].split(sep=',')
                column = ldata.pop(0)
                if "inscription" in column:
                    column = tableurs[0].columns[0]
                if ldata[0] == 'pk':
                    pkey = column
                else:
                    select_req = f'SELECT {ldata[2]} FROM {ldata[0]} AS {ldata[1]} '
                    ldata = ldata[3:]
                    if ldata.pop(0)=='J':
                        select_req += f'JOIN {ldata[0]} AS {ldata[1]} ON {ldata[2]} '
                        ldata = ldata[3:]
                    select_req += f'WHERE {ldata[-1]} = ?'
                    for tabl in tableurs:
                        for i in range(len(tabl)):
                            c.execute('SELECT code FROM candidat WHERE code = ?', (tabl[pkey][i],))
                            if c.fetchone() is not None:
                                c.execute(select_req, (tabl[pkey][i],))
                                res = c.fetchone()
                                if res is not None and tabl[column][i] != res[0]:
                                    print(tabl[pkey][i], column, tabl[column][i], res[0])
            else:
                if 'XXXX.xlsx' in line:
                    nheader = 1
                else:
                    nheader = 0
                tableurs = [pd.read_excel(path/f, header=nheader) if 'xlsx' in f else pd.read_csv(path/f, sep = ";", header=nheader) for f in line[:-1].split(sep=',')]

if __name__ == '__main__':
    pathdb = Path("concours.db")
    db = sql.Connection(pathdb)
    pathfiles = Path('../PPII_ressources/data/public')
    script(db, pathfiles)