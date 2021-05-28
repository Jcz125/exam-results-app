from flask import Flask, Blueprint, render_template, abort, request, redirect, url_for
from flask import g
import sqlite3

app = Flask(__name__)
database= 'DATA.db' # on définie le nom de notre base de données



def getdb():
    db = getattr(g, '_database', None) #On récup la bdd si elle existe, sinon on récup None. g c'est une variable de contexte utilisé par flask. 
    if db is None: #Si on a None, c'est qu'on a pas récup la bdd : il faut donc la récup
        db = g._database = sqlite3.connect(database)
    return db

@app.route("/ecole")
def list_ecole():
    db = getdb()
    c = db.cursor()
    c.execute('SELECT name from ecole')
    l = []
    for i in c.fetchall():
        l.append(i)
    return render_template("liste_ecole.html",liste=l)

@app.route("/etablissement")
def list_etablissement():
    db = getdb()
    c = db.cursor()
    c.execute('SELECT * from etablissement')
    l = []
    for i in c.fetchall():
        l.append(i)
    return render_template("liste_etablissement.html",liste=l)
   




