CREATE TABLE IF NOT EXISTS etat_reponse(
    code INTEGER PRIMARY KEY,
    etat TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ecole(
    code INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS etablissement(
    rne TEXT PRIMARY KEY,
    type TEXT,
    name TEXT NOT NULL,
    cp TEXT,
    ville TEXT,
    pays TEXT
);

CREATE TABLE IF NOT EXISTS concours(
    code INTEGER PRIMARY KEY,
    lib TEXT,
    voie TEXT,
    
    UNIQUE(lib, voie)
);

CREATE TABLE IF NOT EXISTS voeux(
    candidat INTEGER NOT NULL,
    ordre INTEGER CHECK (ordre > 0) NOT NULL,
    ecole INTEGER NOT NULL,

    PRIMARY KEY(candidat, ecole),
    UNIQUE(candidat, ordre),
    FOREIGN KEY(candidat) REFERENCES candidat(code),
    FOREIGN KEY(ecole) REFERENCES ecole(code)
);

CREATE TABLE IF NOT EXISTS classement(
    id INTEGER PRIMARY KEY,
    etudiant INTEGER NOT NULL,
    rang INTEGER CHECK (rang > 0) NOT NULL,
    type INTEGER NOT NULL,

    FOREIGN KEY(etudiant) REFERENCES candidat(code),
    FOREIGN KEY(type) REFERENCES type_classement(id),
    UNIQUE(etudiant, type)
);

CREATE TABLE IF NOT EXISTS type_classement(
    id INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS epreuve(
    id INTEGER PRIMARY KEY,
    lib TEXT NOT NULL,
    type TEXT CHECK (type IN ('ECRIT', 'ORAL', 'SPECIFIQUE', 'CLASSEMENT'))
);

CREATE TABLE IF NOT EXISTS notes(
    candidat INTEGER NOT NULL,
    epreuve INTEGER NOT NULL,
    score REAL NOT NULL,

    PRIMARY KEY(candidat, epreuve),
    FOREIGN KEY(candidat) REFERENCES candidat(code),
    FOREIGN KEY(epreuve) REFERENCES epreuve(id)
);

CREATE TABLE IF NOT EXISTS autre_prenoms(
    etudiant INTEGER NOT NULL,
    prenom TEXT NOT NULL,
    
    PRIMARY KEY(etudiant, prenom)
    FOREIGN KEY(etudiant) REFERENCES candidat(code)
);

CREATE TABLE IF NOT EXISTS pays(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS csp_parent(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS serie_bac(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS etat_dossier(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS ep_option(
    id INTEGER PRIMARY KEY,
    epreuve TEXT NOT NULL,
    option TEXT NOT NULL,

    UNIQUE(epreuve, option)
);

CREATE TABLE IF NOT EXISTS civilite(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS classe(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS candidat(
    code INTEGER PRIMARY KEY,
    civ INTEGER,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_de_naissance DATE,
    classe TEXT,
    puissance TEXT CHECK(puissance IN ('3/2', '5/2', '7/2')),
    voie_concours INTEGER,
    etablissement TEXT,
    adresse1 TEXT,
    adresse2 TEXT,
    code_postal TEXT,
    commune TEXT,
    code_adr_pays INTEGER,
    mail TEXT,
    tel TEXT,
    por TEXT,
    code_pays_naissance INTEGER,
    code_pays_nationalite INTEGER,
    ville_ecrit TEXT,
    ine TEXT UNIQUE,
    csp_pere INTEGER,
    csp_mere INTEGER,

    bac INTEGER,
    annee_bac INTEGER,
    mois_bac INTEGER,
    mention_bac TEXT CHECK(mention_bac IN ('TB', 'B', 'AB', 'S')),
    dep_bac INTEGER,

    dossier INTEGER,
    qualite TEXT,
    decla_handicap INTEGER DEFAULT 0 CHECK(decla_handicap IN (0, 1)),
    arr_naissance INTEGER DEFAULT 0,

    option1 INTEGER,
    option2 INTEGER,
    option3 INTEGER,
    option4 INTEGER,
    tipe TEXT,

    etat_classes INTEGER,
    type_admissible TEXT,

    FOREIGN KEY(voie_concours) REFERENCES concours(code),
    FOREIGN KEY(etablissement) REFERENCES etablissement(rne),
    FOREIGN KEY(code_adr_pays) REFERENCES pays(code),
    FOREIGN KEY(code_pays_naissance) REFERENCES pays(code),
    FOREIGN KEY(code_pays_nationalite) REFERENCES pays(code),
    FOREIGN KEY(csp_pere) REFERENCES csp_parent(code),
    FOREIGN KEY(csp_mere) REFERENCES csp_parent(code),
    FOREIGN KEY(bac) REFERENCES serie_bac(code),
    FOREIGN KEY(dossier) REFERENCES etat_dossier(code),
    FOREIGN KEY(option1) REFERENCES ep_option(id),
    FOREIGN KEY(option2) REFERENCES ep_option(id),
    FOREIGN KEY(option3) REFERENCES ep_option(id),
    FOREIGN KEY(option4) REFERENCES ep_option(id)
    FOREIGN KEY(civ) REFERENCES civilite(code)
);
