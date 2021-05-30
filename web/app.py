from flask import Flask, Blueprint, render_template, abort, request, redirect, url_for
from flask import g
import sqlite3

app = Flask(__name__)
database= 'concours.db' # on définie le nom de notre base de données



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

@app.route("/epreuve")
def list_epreuve():
    db = getdb()
    c = db.cursor()
    c.execute('SELECT lib,type from epreuve WHERE id<10000')
    l = []
    for i in c.fetchall():
        l.append(i)
    return render_template("liste_epreuve.html",liste=l)
   
@app.route("/option")
def list_option():
    db = getdb()
    c = db.cursor()
    c.execute('SELECT epreuve,option from ep_option')
    l = []
    for i in c.fetchall():
        l.append(i)
    return render_template("liste_option.html",liste=l)

@app.route("/csp")
def list_csp():
    db = getdb()
    c = db.cursor()
    c.execute('SELECT lib from csp_parent')
    l = []
    for i in c.fetchall():
        l.append(i)
    return render_template("liste_csp.html",liste=l)
 

@app.route("/candidatByCode/<code>") ####RESTE LES CLASSEMENTS
def rech_can_name(code):
    db = getdb()
    c = db.cursor()
    c.execute("SELECT * from candidat WHERE code=(?)",(code,))
    l = []
    cv=[]
    for i in c.fetchall():
        l.append(i)
    ##civilite
    cv=[]
    for i in l:
        c=db.cursor()
        c.execute("SELECT lib from civilite WHERE code=(?)",(i[1],))
        for i in c.fetchall():
            cv.append(i[0])
    ###autre_prenoms
    autre_prenoms=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT prenom from autre_prenoms WHERE etudiant=(?)",(i[0],))
        for i in c.fetchall():
            autre_prenoms.append(i[0])
    if autre_prenoms == []:
        autre_prenoms.append("")

    ###classe
    cl=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from classe WHERE code=(?)",(i[5],))
        for i in c.fetchall():
            cl.append(i[0])

    ###voie
    voie=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT voie from concours WHERE code=(?)",(i[7],))
        for i in c.fetchall():
            voie.append(i[0])

    ###etablissement
    etablissement=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT name from etablissement WHERE rne=(?)",(i[8],))
        for i in c.fetchall():
            etablissement.append(i[0])
    ###code_adr_pays
    pays=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from pays WHERE code=(?)",(i[13],))
        for i in c.fetchall():
            pays.append(i[0])
    ###code_pays_naissance
    pays_naissance=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from pays WHERE code=(?)",(i[17],))
        for i in c.fetchall():
            pays_naissance.append(i[0])
    ###code_pays_nationalite
    pays_nationalite=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT nationalite from pays WHERE code=(?)",(i[19],))
        for i in c.fetchall():
            pays_nationalite.append(i[0])
    ###csp_pere
    csp_pere=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from csp_parent WHERE code=(?)",(i[22],))
        for i in c.fetchall():
            csp_pere.append(i[0])
    ###csp_mere
    csp_mere=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from csp_parent WHERE code=(?)",(i[23],))
        for i in c.fetchall():
            csp_mere.append(i[0])
    ###bac
    bac=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from serie_bac WHERE code=(?)",(i[24],))
        for i in c.fetchall():
            bac.append(i[0])
    ###dossier
    dossier=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT lib from etat_dossier WHERE code=(?)",(i[29],))
        for i in c.fetchall():
            dossier.append(i[0])
    ###option1
    option1=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT option from ep_option WHERE id=(?)",(i[33],))
        for i in c.fetchall():
            option1.append(i[0])
    if option1 == []:
        option1.append("")
    ###option2
    option2=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT option from ep_option WHERE id=(?)",(i[34],))
        for i in c.fetchall():
            option2.append(i[0])
    if option2 == []:
        option2.append("")
    ###option3
    option3=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT option from ep_option WHERE id=(?)",(i[35],))
        for i in c.fetchall():
            option3.append(i[0])
    if option3 == []:
        option3.append("")
    ###option4
    option4=[]
    for i in l:
        c= db.cursor()
        c.execute("SELECT option from ep_option WHERE id=(?)",(i[36],))
        for i in c.fetchall():
            option4.append(i[0])
    if option4 == []:
        option4.append("")

    return render_template("liste_candidat.html",liste=l,civ=cv[0],classe=cl[0],voie=voie[0],etablissement=etablissement[0],pays=pays[0],pays_naissance=pays_naissance[0],pays_nationalite=pays_nationalite[0],csp_pere=csp_pere[0],csp_mere=csp_mere[0],bac=bac[0],dossier=dossier[0],option1=option1[0],option2=option2[0],option3=option3[0],option4=option4[0],autre_prenoms=autre_prenoms[0])
 
