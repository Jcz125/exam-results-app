import openpyxl as xl
import sqlite3 as sql
from pathlib import Path

db = sql.connect("concours.db")

for classe in ("MP", "TSI", "PT", "ATS", "PC", "PSI"):
    file = xl.load_workbook(Path(f"../PPII_ressources/data/public/listeVoeux_{classe}.xlsx"), read_only=True)
    tab = file[file.sheetnames[0]]

    with db:
        c = db.cursor()
        rows = tab.rows
        next(rows)
        for line in rows:
            c.execute("INSERT OR IGNORE INTO voeux VALUES (?,?,?)", (line[0].value, line[2].value, line[3].value))
    file.close()

db.close()