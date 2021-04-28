import sqlite3 as sql
import openpyxl as xl
from pathlib import Path
import click

#on peut faire de la ligne de commande avec click


def test_etat_reponse_appel(path_db, path_dir):
    path_file = path_dir/Path("listeEtatsReponsesAppel.xlsx")

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
        click.echo("Fin")
    except sql.DatabaseError as e:
        click.echo(e,err=True)
    finally:
        con.close()


def init_bd(path_db, path_init):
    with open(path_init, "r") as f_init:
        try:
            con = sql.connect(path_db)
            with con:
                con.executescript(f_init.read())
        except sql.DatabaseError as e:
            print(e)
        finally:
            con.close()


@click.command()
@click.argument("database", type=click.Path(dir_okay=False))
@click.argument("src_dir", type=click.Path(exists=True, file_okay=False))
@click.option("--init", "-i", default=None, type=click.Path(exists=True, dir_okay=False))
def cli(database, src_dir, init):
    database = Path(database)
    src_dir = Path(src_dir)
    if init is not None:
        init = Path(init)
        click.echo(f"Initialisation de {database.name} avec {init.name}")
        init_bd(database,init)
    click.echo("Importation de listeEtatsReponsesAppel.xlsx")
    test_etat_reponse_appel(database, src_dir)
