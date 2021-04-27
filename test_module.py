import sqlite3 as sql
import openpyxl as xl
from pathlib import Path

#on peut faire de la ligne de commande avec click


def test_etat_reponse_appel(path_db, path_file):
    path_db = Path(path_db)
    path_file = Path(path_file)/Path("listeEtatsReponsesAppel.xlsx")

    try:
        con = sql.connect(path_db)
        file = xl.load_workbook(path_file, read_only=True)
        tab = file["Export Workbook"]

        rows = tab.rows
        next(rows)
        for line in rows:
            with con:
                con.execute("INSERT INTO etat_reponse VALUES(?,?)", (line[0].value, line[1].value))
        file.close()
    except sql.DatabaseError as e:
        print(e)
    finally:
        con.close()



if __name__=="__main__":
    test_etat_reponse_appel("dbtest.db", "../PPII_ressources/data/public")