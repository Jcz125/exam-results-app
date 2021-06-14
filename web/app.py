from flask import Flask, Blueprint, render_template, abort, request, redirect, url_for
from flask import g
import sqlite3
from numpy import *

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


# @app.route("/moyenne/<codepreuve>/<rne>") ### moyenne de l'epreuve  numéro 'codepreuve' des candidats de letab numero 'rne'
# def moyenne_epreuve_etablissement(codepreuve,rne):
#     db = getdb()
#     c = db.cursor()
#     c.execute('SELECT * from notes WHERE epreuve=(?);', (codepreuve,))
#     l = []
#     for i in c.fetchall():
#         l.append(i)
#     c = db.cursor()
#     c.execute('SELECT code from candidat WHERE etablissement=(?);', (rne,))
#     h=[]
#     for i in c.fetchall():
#         h.append(i)
#     out = [item for t in h for item in t] #convert list of tuples into list
#     total = []
#     for i in l :
#         if i[0] in out :
#             total.append(i)
#     somme = 0
#     for i in total:
#         somme = somme + i[2]
#     if len(total) != 0 :
#         moyenne = round(somme/len(total),2)
#     else :
#         moyenne = "Aucun candidat de l'établissement n'a passé cet épreuve"
#     ####recuperer des infos sur l'epreuve et l'etablissement
#     db = getdb()
#     c = db.cursor()
#     c.execute('SELECT * from epreuve WHERE id=(?);', (codepreuve,))
#     ep=[]
#     for i in c.fetchall():
#         ep.append(i)
#         db = getdb()
#     c = db.cursor()
#     c.execute('SELECT name,ville from etablissement WHERE etablissement.rne=(?);', (rne,))
#     etab=[]
#     for i in c.fetchall():
#         etab.append(i)
#     return render_template("stats_epreuve_etab.html", moyenne = moyenne, epreuve=ep , etablissement = etab)


def calcul_stats(L):
    val = []
    for k in L:
        val.append(k[0])
    moy = round(mean(val), 2)
    Q1 = quantile(val, 0.25)
    med = median(val)
    Q3 = quantile(val, 0.75)
    sigma = 0
    for i in val:
        sigma += i**2
    sigma = round(sqrt(sigma/len(val) - moy**2), 2)
    return [moy, Q1, med, Q3, sigma, len(val)]


@app.route("/stats/<id_epreuve>/<filiere>/") ### stats de l'épreuve numéro id_epreuve des candidats dans la filière filiere
def stats_epreuve_par_filiere(id_epreuve, filiere):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT * FROM epreuve WHERE id=(?);', (id_epreuve,))
    epreuve = c.fetchall()[0]
    if filiere == "all":
        c.execute('SELECT score FROM notes WHERE epreuve=(?);', (id_epreuve,))
        stats = calcul_stats(c.fetchall())
        return render_template("stats_epreuve_filiere.html", moyenne=stats[0], Q1=stats[1], Q2=stats[2], Q3=stats[3], sigma=stats[4], nb_can=stats[5], epreuve=epreuve, filiere="")
    else:
        c.execute('SELECT score FROM notes JOIN epreuve ON id=epreuve JOIN candidat ON candidat.code=candidat JOIN concours ON concours.code=voie_concours WHERE concours.voie=(?) AND epreuve.id=(?);', (filiere, id_epreuve))
        stats = calcul_stats(c.fetchall())
        return render_template("stats_epreuve_filiere.html", moyenne=stats[0], Q1=stats[1], Q2=stats[2], Q3=stats[3], sigma=stats[4], nb_can=stats[5], epreuve=epreuve, filiere=filiere)


@app.route("/stats/<id_epreuve>/<filiere>/<rne>") ### stats de l'epreuve numéro id_epreuve des candidats de l'établissement numéro rne de la filière filiere
def stats_epreuve_par_filiere_par_etablissement(id_epreuve, filiere, rne):
    db = getdb()
    c = db.cursor()
    c.execute('SELECT * FROM epreuve WHERE id=(?);', (id_epreuve,))
    epreuve = c.fetchall()[0]
    c.execute('SELECT rne, name, ville FROM etablissement WHERE rne=(?);', (rne,))
    etablissement = c.fetchall()[0]
    if filiere == "all":
        c.execute('SELECT score FROM notes JOIN epreuve ON id=epreuve JOIN candidat ON candidat.code=candidat WHERE epreuve.id=(?) AND etablissement=(?);', (id_epreuve, rne))
        res = c.fetchall()
        if len(res) != 0:
            stats = calcul_stats(res)
            return render_template("stats_epreuve_etab.html", moyenne=stats[0], Q1=stats[1], Q2=stats[2], Q3=stats[3], sigma=stats[4], nb_can=stats[5], epreuve=epreuve, filiere="", etablissement=etablissement)
        else:
            return "Pas de résultat"
    else:
        c.execute('SELECT score FROM notes JOIN epreuve ON id=epreuve JOIN candidat ON candidat.code=candidat JOIN concours ON concours.code=voie_concours WHERE concours.voie=(?) AND epreuve.id=(?) AND etablissement=(?);', (filiere, id_epreuve, rne))
        res = c.fetchall()
        if len(res) != 0:
            stats = calcul_stats(res)
            return render_template("stats_epreuve_etab.html", moyenne=stats[0], Q1=stats[1], Q2=stats[2], Q3=stats[3], sigma=stats[4], nb_can=stats[5], epreuve=epreuve, filiere=filiere, etablissement=etablissement)
        else:
            return "Pas de résultat"


dico_ep = {
    ("ECRIT", "MP"): [28, 599, 600, 601, 602, 603, 604, 605, 1050, 9898, 9899],
    ("ORAL", "MP"): [5, 6, 7, 8, 9, 10, 11, 12, 400, 401, 9900, 9901, 9998, 9999],
    ("SPECIFIQUE", "MP"): [1, 2, 3, 4],
    ("CLASSEMENT", "MP"): [10198, 10199, 10200, 10201],
    ("ECRIT", "PC"): [28, 599, 600, 601, 602, 603, 604, 605, 1050, 9898, 9899],
    ("ORAL", "PC"): [5, 6, 7, 8, 9, 10, 11, 12, 400, 401, 9900, 9901, 9998, 9999],
    ("SPECIFIQUE", "PC"): [1, 2, 3, 4],
    ("CLASSEMENT", "PC"): [10198, 10199, 10200, 10201],
    ("ECRIT", "PSI"): [28, 600, 601, 602, 603, 604, 605, 606, 1050, 9898, 9899],
    ("ORAL", "PSI"): [5, 6, 7, 8, 9, 10, 11, 12, 400, 401, 9900, 9901, 9998, 9999],
    ("SPECIFIQUE", "PSI"): [1, 2, 3, 4],
    ("CLASSEMENT", "PSI"): [10198, 10199, 10200, 10201],
    ("ECRIT", "PT"): [700, 701, 702, 703, 704, 705, 706, 707, 9898, 9899],
    ("ORAL", "PT"): [5, 6, 7, 8, 400, 401, 9900, 9901, 9998, 9999],
    ("SPECIFIQUE", "PT"): [1, 2, 3, 4],
    ("CLASSEMENT", "PT"): [10198, 10199, 10200, 10201],
    ("ECRIT", "TSI"): [800, 801, 802, 803, 804, 805, 806, 807, 9898, 9899],
    ("ORAL", "TSI"): [14, 15, 16, 17, 18, 19, 400, 401, 9998, 9999],
    ("SPECIFIQUE", "TSI"): [1, 2, 3, 4],
    ("CLASSEMENT", "TSI"): [10198, 10199, 10201],
    ("ECRIT", "ATS"): [9899, 9897, 9898, 956, 957, 958, 959, 960],
    ("ORAL", "ATS"): [9997, 9998, 961, 962, 963, 964, 981, 1030],
}

def find_eps(type, filiere):
    if type == "":
        return [10000]
    else:
        return dico_ep[(type, filiere)]
    # elif filiere == "MP":
    #     if type == "ECRIT":
    #         return liste_ep_MP_ecrits
    #     elif type == "ORAL":
    #         return liste_ep_MP_oraux
    #     elif type == "SPECIFIQUE":
    #         return liste_ep_MP_spe
    #     elif type == "CLASSEMENT":
    #         return liste_ep_MP_class
    # elif filiere == "PC":
    #     if type == "ECRIT":
    #         return liste_ep_PC_ecrits
    #     elif type == "ORAL":
    #         return liste_ep_PC_oraux
    #     elif type == "SPECIFIQUE":
    #         return liste_ep_PC_spe
    #     elif type == "CLASSEMENT":
    #         return liste_ep_PC_class
    # elif filiere == "PSI":
    #     if type == "ECRIT":
    #         return liste_ep_PSI_ecrits
    #     elif type == "ORAL":
    #         return liste_ep_PSI_oraux
    #     elif type == "SPECIFIQUE":
    #         return liste_ep_PSI_spe
    #     elif type == "CLASSEMENT":
    #         return liste_ep_PSI_class
    # elif filiere == "PT":
    #     if type == "ECRIT":
    #         return liste_ep_PT_ecrits
    #     elif type == "ORAL":
    #         return liste_ep_PT_oraux
    #     elif type == "SPECIFIQUE":
    #         return liste_ep_PT_spe
    #     elif type == "CLASSEMENT":
    #         return liste_ep_PT_class
    # elif filiere == "TSI":
    #     if type == "ECRIT":
    #         return liste_ep_TSI_ecrits
    #     elif type == "ORAL":
    #         return liste_ep_TSI_oraux
    #     elif type == "SPECIFIQUE":
    #         return liste_ep_TSI_spe
    #     elif type == "CLASSEMENT":
    #         return liste_ep_TSI_class
    # elif filiere == "ATS":
    #     if request.form.get("type") == "ECRIT":
    #         return liste_ep_ATS_ecrits
    #     elif request.form.get("type") == "ORAL":
    #         return liste_ep_ATS_oraux


@app.route("/stats_forms", methods=["get", "post"]) ### recherche identique à la précédente mais par form,
# en sélectionnant d'abord la filière puis le type de l'épreuve, une liste s'actualise,
# puis on peut choisir l'épreuve concernée et le rne de l'établissement
def stats_forms():
    print(request.form)
    if request.method == "GET":
        return render_template("stats_forms.html")
    elif request.method == "POST" and request.form.get("button") == "1":
        db = getdb()
        c = db.cursor()
        c.execute('SELECT id from epreuve WHERE epreuve.type = (?) and lib = (?);',
            (request.form.get("type"), request.form.get("epreuve")))
        for i in c.fetchall():
            if i[0] in find_eps(request.form.get("type"), request.form.get("filiere")):
                return redirect(f"/stats/{i[0]}/{request.form.get('filiere')}/{request.form.get('etablissement')}")
        return "Pas d'épreuve trouvée"
    else:
        db = getdb()
        c = db.cursor()
        epreuves = find_eps(request.form.get("type"), request.form.get("filiere"))
        lib_epreuves = []
        if epreuves:
            for k in epreuves:
                c.execute('SELECT lib from epreuve WHERE epreuve.id = (?);', (k,))
                lib_epreuves.append(c.fetchall()[0][0])
        return render_template("stats_forms.html", epreuves=lib_epreuves, filiere_select=request.form.get("filiere"),
            type_select=request.form.get("type"))


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

@app.route("/")
def home():
    return render_template("index.html")



