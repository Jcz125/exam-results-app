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
    c.execute('SELECT code , name from ecole')
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
    c.execute('SELECT id,lib,type from epreuve WHERE id<10000')
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
    c.execute('SELECT * from csp_parent')
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
 

@app.route("/voeux/<code>") ### une page qui contient un tableau des voeux du candidat
def candidat_voeux(code):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT ordre,ecole from voeux WHERE candidat=(?)', (code,))
    l = []
    for i in c.fetchall():
        l.append(i)
    ###ecole
    longueur=len(l)
    nbecole=[]
    nomecole=[]
    for i in range(longueur):
        nbecole.append(l[i][1])
    for i in range(longueur):
        db = getdb()
        c = db.cursor()
        c.execute('SELECT name from ecole WHERE code=(?)', (nbecole[i],))
        for k in c.fetchall():
            nomecole.append(k)
    final=[]
    for i in range(longueur):
        tuple= (l[i][0], nomecole[i][0])
        final.append(tuple)
    return render_template("liste_voeux.html", liste = l , nomecole = nomecole, final = final)


@app.route("/notes/<code>") ### notes du candidat numéro 'code'
def candidat_notes(code):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT epreuve,score from notes WHERE candidat=(?)', (code,))
    l = []
    for i in c.fetchall():
        l.append(i)
    ###nom epreuve
    longueur=len(l)
    nbepreuve=[]
    nomeepreuve=[]
    for i in range(longueur):
        nbepreuve.append(l[i][0])
    for i in range(longueur):
        db = getdb()
        c = db.cursor()
        c.execute('SELECT lib , type from epreuve WHERE id=(?)', (nbepreuve[i],))
        for k in c.fetchall():
            nomeepreuve.append(k)
    final=[]
    for i in range(longueur):
        tuple= (nomeepreuve[i][0], nomeepreuve[i][1] , l[i][1])
        final.append(tuple)
    return render_template("liste_notes.html", liste = l , final = final)


@app.route("/classement/<code>") ### classement du candidat numéro 'code'
def candidat_classement(code):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT rang , type from classement WHERE etudiant=(?)', (code,))
    l = []
    for i in c.fetchall():
        l.append(i)
    ###nom epreuve
    longueur=len(l)
    nbtype=[]
    nomtype=[]
    for i in range(longueur):
        nbtype.append(l[i][1])
    for i in range(longueur):
        db = getdb()
        c = db.cursor()
        c.execute('SELECT lib  from type_classement WHERE id=(?)', (nbtype[i],))
        for k in c.fetchall():
            nomtype.append(k)
    final=[]
    for i in range(longueur):
        tuple= (nomtype[i][0], l[i][0])
        final.append(tuple)
    return render_template("liste_classement.html", liste = l , final = final)


@app.route("/rech", methods=["get", "post"])
def rech():
    if not request.method == "POST" and not request.form.get("candidat_name"):
        return render_template("rech_candidat.html")
    else:
        db = getdb()
        c = db.cursor()
        c.execute('SELECT code , civ , nom , prenom FROM candidat where nom LIKE (?)', ("%" + request.form.get("candidat_name") + "%",))
        l = []
        for i in c.fetchall():
            l.append(i)
        return render_template("result_rech.html", liste=l)


@app.route("/moyenne/<codepreuve>/<rne>") ### moyenne de l'epreuve  numéro 'codepreuve' des candidats de letab numero 'rne'
def moyenne_epreuve_etablissement(codepreuve,rne):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT * from notes WHERE epreuve=(?)', (codepreuve,))
    l = []
    for i in c.fetchall():
        l.append(i)
    c = db.cursor()
    c.execute('SELECT code from candidat WHERE etablissement=(?)', (rne,))
    h=[]
    for i in c.fetchall():
        h.append(i)
    out = [item for t in h for item in t] #convert list of tuples into list
    total = []
    for i in l :
        if i[0] in out :
            total.append(i)
    somme = 0
    for i in total:
        somme = somme + i[2]
    if len(total) != 0 :
        moyenne = round(somme/len(total),2)
    else :
        moyenne = "Aucun candidat de l'établissement n'a passé cet épreuve"
    ####recuperer des infos sur l'epreuve et l'etablissement
    db = getdb()
    c = db.cursor()
    c.execute('SELECT * from epreuve WHERE id=(?)', (codepreuve,))
    ep=[]
    for i in c.fetchall():
        ep.append(i)
        db = getdb()
    c = db.cursor()
    c.execute('SELECT name,ville from etablissement WHERE etablissement.rne=(?)', (rne,))
    etab=[]
    for i in c.fetchall():
        etab.append(i)
    return render_template("moyenne_epreuve_etab.html", moyenne = moyenne, epreuve=ep , etablissement = etab)


@app.route("/moyenne_forms", methods=["get", "post"])
def moyenne_forms():
    if not request.method == "POST" and not request.form.get("epreuve") and not request.form.get("etablissement") and not request.form.get("type"):
        db = getdb()
        c = db.cursor()
        c.execute('SELECT epreuve.type from epreuve')
        types = []
        for i in c.fetchall():
            types.append(i)
        types = list(set(types)) #to avoid duplicate
        # types.sort()
        return render_template("moyenne_forms.html", var=request.form.get("type"))
    if not request.method == "POST" or not request.form.get("epreuve") or not request.form.get("etablissement"):
        db = getdb()
        c = db.cursor()
        c.execute('SELECT lib from epreuve WHERE epreuve.type = (?)', (""+request.form.get("type"),))
        epreuves = []
        for i in c.fetchall():
            epreuves.append(i)
        return render_template("moyenne_forms.html", epreuves=epreuves)
    else:
        db = getdb()
        c = db.cursor()
        c.execute('SELECT id from epreuve WHERE epreuve.type = (?) and lib = (?)', (request.form.get("type"), request.form.get("epreuve")))
        id = []
        for i in c.fetchall():
            id.append(i)
        return moyenne_epreuve_etablissement(id[0][0],request.form.get("etablissement"))


# Autre version de classement par popularité voeux des écoles
# @app.route("/ecole_populaire", methods=["get", "post"]) ### les top n écoles les plus choisies, ecole = code de l'école
# def ecole_populaire():
#     db = getdb()
#     c = db.cursor()
#     ecoles = {}
#     c.execute('SELECT * FROM ecole;')
#     for k in c.fetchall():
#         ecoles[k[0]] = k[1]
#
#     iteration = []
#     for i in ecoles:
#         c.execute('SELECT COUNT(ecole) FROM voeux WHERE ecole = (?);', (i,))
#         cpt = c.fetchall()
#         iteration.append((i, int(cpt[0][0])))
#
#     iteration.sort(key = lambda x: x[1], reverse=True)
#
#     return render_template("liste_popularite.html", iteration=iteration, ecoles=ecoles)


@app.route("/voeuxparecole")
def voeux_ecole():
    tri = request.args.get("order",default=None)
    tri_state = {"ordre": "AVG(v.ordre)", "name": "e.name", "number": "COUNT(v.candidat)"}.get(tri)
    if tri_state is None:
        tri = "ordre"
        tri_state = "AVG(v.ordre)"
    sens = request.args.get("sens", default=None)
    if sens not in ("ASC", "DESC"):
        sens = "ASC"
    db = getdb()
    c = db.cursor()
    c.execute(f'SELECT e.name,COUNT(v.candidat),AVG(v.ordre) FROM ecole as e JOIN voeux as v ON e.code=v.ecole GROUP BY e.name ORDER BY {tri_state} {sens}')
    return render_template("voeux_ecole.html", liste=list(c.fetchall()), choice=(tri, sens))



