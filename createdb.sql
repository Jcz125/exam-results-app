CREATE TABLE etat_reponse (
    code INTEGER PRIMARY KEY,
    etat TEXT NOT NULL
);

CREATE TABLE ecole (
    code INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE etablissement(
    rne TEXT PRIMARY KEY,
    type TEXT,
    name TEXT,
    cp TEXT,
    ville TEXT,
    pays TEXT
);

CREATE TABLE concours(
    code INTEGER PRIMARY KEY,
    lib TEXT,
    voie TEXT,

    UNIQUE(lib, voie)
);

CREATE TABLE voeux(
    candidat INTEGER,
    ordre INTEGER CHECK (ordre > 0),
    ecole INTEGER,

    PRIMARY KEY(candidat, ecole),
    UNIQUE(candidat, ordre),
    FOREIGN KEY(candidat) REFERENCES candidat(code),
    FOREIGN KEY(ecole) REFERENCES ecole(code)
);

CREATE TABLE classement(
    id INTEGER PRIMARY KEY,
    etudiant INTEGER,
    rang INTEGER CHECK (rang > 0),
    type TEXT,

    FOREIGN KEY(etudiant) REFERENCES candidat(code)
);

CREATE TABLE epreuve(
    id INTEGER,
    lib TEXT,
    type TEXT CHECK IN ('ECRIT', 'ORAL')
);

CREATE TABLE notes(
    candidat INTEGER,
    epreuve INTEGER,
    score INTEGER,

    PRIMARY KEY(candidat, epreuve),
    FOREIGN KEY(candidat) REFERENCES candidat(code),
    FOREIGN KEY(epreuve) REFERENCES epreuve(id)
);

CREATE TABLE autres_prenoms(
    etudiant INTEGER,
    prenom TEXT,
    
    PRIMARY KEY(etudiant, prenom)
    FOREIGN KEY(etudiant) REFERENCES candidat(code)
);

CREATE TABLE pays(
    code INTEGER PRIMARY KEY,
    lib TEXT
);

CREATE TABLE csp_parent(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE
);

CREATE TABLE serie_bac(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE
);

CREATE TABLE etat_dossier(
    code INTEGER PRIMARY KEY,
    lib TEXT UNIQUE
);

CREATE TABLE ep_option(
    id INTEGER PRIMARY KEY,
    epreuve TEXT,
    option TEXT,

    UNIQUE(epreuve, option)
);

CREATE TABLE candidat(
    code INTEGER PRIMARY KEY,
    civilite TEXT CHECK(civilite IN ('M.', 'Mme')),
    nom TEXT,
    prenom TEXT,
    date_de_naissance DATE,
    classe TEXT CHECK(classe IN ('MP', 'MP*', 'PC', 'PC*', 'PSI', 'PSI*', 'TSI', 'TSI*', 'PT', 'PT*')),
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
    qualite TEXT CHECK(qualite IN ('Boursier')),
    decla_handicap INTEGER DEFAULT 0 CHECK(decla_handicap IN (0, 1)),
    arr_naissance INTEGER DEFAULT 0,

    option1 INTEGER,
    option2 INTEGER,
    option3 INTEGER,
    option4 INTEGER,
    tipe TEXT,

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
);
