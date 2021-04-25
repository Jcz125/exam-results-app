CREATE TABLE etat_reponse (
    code INTEGER PRIMARY KEY,
    etat TEXT NOT NULL
)

CREATE TABLE ecole (
    code INTEGER PRIMARY KEY,
    name TEXT
)

CREATE TABLE etablissement(
    rne TEXT PRIMARY KEY,
    type TEXT,
    name TEXT,
    cp INTEGER,
    ville TEXT,
    pays TEXT,
)

CREATE TABLE concours(
    code INTEGER PRIMARY KEY,
    lib TEXT,
    voie TEXT
)

CREATE TABLE voeux(
    candidat INTEGER,
    ordre INTEGER,
    ecole INTEGER,
    PRIMARY KEY(candidat, ecole),
    UNIQUE(candidat, ordre),
)
