DROP TABLE IF EXISTS Region;
DROP TABLE IF EXISTS EdInst;
DROP TABLE IF EXISTS Human;
DROP TABLE IF EXISTS Ukr;
DROP TABLE IF EXISTS Hist;
DROP TABLE IF EXISTS Math;
DROP TABLE IF EXISTS Phys;
DROP TABLE IF EXISTS Chem;
DROP TABLE IF EXISTS Bio;
DROP TABLE IF EXISTS Geo;
DROP TABLE IF EXISTS Eng;
DROP TABLE IF EXISTS Fra;
DROP TABLE IF EXISTS Deu;
DROP TABLE IF EXISTS Spa;

CREATE TABLE Region (
        reg_id SERIAL,
	RegName VARCHAR(255),
	AreaName VARCHAR(255),
	TerName VARCHAR(255),
	TerTypeName VARCHAR(50)
);
ALTER TABLE Region ADD CONSTRAINT Region_pk PRIMARY KEY (reg_id);


CREATE TABLE EdInst (
        eo_id SERIAL,
	EOName VARCHAR(255),
	EOTypeName VARCHAR(255),
	EORegName VARCHAR(255),
	EOAreaName VARCHAR(255),
	EOTerName VARCHAR(255),
	EOParent VARCHAR(255)
);
ALTER TABLE EdInst ADD CONSTRAINT EO_pk PRIMARY KEY (eo_id);


CREATE TABLE Human (
	OUTID VARCHAR(50),
	Birth INT,
	SexTypeName VARCHAR(50),
	Year INT,
	RegTypeName VARCHAR(255),
	ClassProfileName VARCHAR(255),
	ClassLangName VARCHAR(255),
        reg_id SERIAL,
        eo_id SERIAL
);
ALTER TABLE Human ADD CONSTRAINT Human_pk PRIMARY KEY (OUTID);

ALTER TABLE Human
    ADD CONSTRAINT Human_fk FOREIGN KEY (reg_id)
        REFERENCES Region (reg_id);
ALTER TABLE Human
    ADD CONSTRAINT Human_fk2 FOREIGN KEY (eo_id)
        REFERENCES EdInst (eo_id);


CREATE TABLE Ukr (
	OUTID VARCHAR(50),
	UkrTest	VARCHAR(255),
	UkrTestStatus VARCHAR(255),
	UkrBall100 REAL,
	UkrBall12 REAL,
	UkrBall	REAL,
	UkrAdaptScale FLOAT,
	UkrPTName VARCHAR(255),
	UkrPTRegName VARCHAR(255),
	UkrPTAreaName VARCHAR(255),
	UkrPTTerName VARCHAR(255)
);
ALTER TABLE Ukr ADD CONSTRAINT Ukr_pk PRIMARY KEY (OUTID, UkrTest);

ALTER TABLE Ukr
    ADD CONSTRAINT Ukr_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Hist (
	OUTID VARCHAR(50),
	histTest VARCHAR(255),
	HistLang VARCHAR(255),
	histTestStatus VARCHAR(255),
	histBall100 REAL,
	histBall12 REAL,
	histBall REAL,
	histPTName VARCHAR(255),
	histPTRegName VARCHAR(255),
	histPTAreaName VARCHAR(255),
	histPTTerName VARCHAR(255)
);
ALTER TABLE Hist ADD CONSTRAINT Hist_pk PRIMARY KEY (OUTID, histTest);

ALTER TABLE Hist 
    ADD CONSTRAINT Hist_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Math (
	OUTID VARCHAR(50),
	mathTest VARCHAR(255),
	mathLang VARCHAR(255),
	mathTestStatus VARCHAR(255),
	mathBall100 REAL,
	mathBall12 REAL,math
	mathBall REAL,
	mathPTName VARCHAR(255),
	mathPTRegName VARCHAR(255),
	mathPTAreaName VARCHAR(255),
	mathPTTerName VARCHAR(255)
);
ALTER TABLE Math ADD CONSTRAINT Math_pk PRIMARY KEY (OUTID, mathTest);

ALTER TABLE Math
    ADD CONSTRAINT Math_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Phys (
	OUTID VARCHAR(50),
	physTest VARCHAR(255),
	physLang VARCHAR(255),
	physTestStatus VARCHAR(255),
	physBall100 REAL,
	physBall12 REAL,
	physBall REAL,
	physPTName VARCHAR(255),
	physPTRegName VARCHAR(255),
	physPTAreaName VARCHAR(255),
	physPTTerName VARCHAR(255)
);
ALTER TABLE Phys ADD CONSTRAINT Phys_pk PRIMARY KEY (OUTID, physTest);

ALTER TABLE Phys
    ADD CONSTRAINT Phys_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);



CREATE TABLE Chem (
	OUTID VARCHAR(50),
	chemTest VARCHAR(255),
	chemLang VARCHAR(255),
	chemTestStatus VARCHAR(255),
	chemBall100 REAL,
	chemBall12 REAL,
	chemBall REAL,
	chemPTName VARCHAR(255),
	chemPTRegName VARCHAR(255),
	chemPTAreaName VARCHAR(255),
	chemPTTerName VARCHAR(255)
);
ALTER TABLE Chem ADD CONSTRAINT Chem_pk PRIMARY KEY (OUTID, chemTest);

ALTER TABLE Chem
    ADD CONSTRAINT Chem_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Bio (
	OUTID VARCHAR(50),
	bioTest VARCHAR(255),
	bioLang VARCHAR(255),
	bioTestStatus VARCHAR(255),
	bioBall100 REAL,
	bioBall12 REAL,
	bioBall	REAL,
	bioPTName VARCHAR(255),
	bioPTRegName VARCHAR(255),
	bioPTAreaName VARCHAR(255),
	bioPTTerName VARCHAR(255)
);
ALTER TABLE Bio ADD CONSTRAINT Bio_pk PRIMARY KEY (OUTID, bioTest);

ALTER TABLE Bio
    ADD CONSTRAINT Bio_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);



CREATE TABLE Geo (
	OUTID VARCHAR(50),
	geoTest VARCHAR(255),
	geoLang VARCHAR(255),
	geoTestStatus VARCHAR(255),
	geoBall100 REAL,
	geoBall12 REAL,
	geoBall	REAL,
	geoPTName VARCHAR(255),
	geoPTRegName VARCHAR(255),
	geoPTAreaName VARCHAR(255),
	geoPTTerName VARCHAR(255)
);
ALTER TABLE Geo ADD CONSTRAINT Geo_pk PRIMARY KEY (OUTID, geoTest);

ALTER TABLE Geo
    ADD CONSTRAINT Geo_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Eng (
	OUTID VARCHAR(50),
	engTest VARCHAR(255),
	engTestStatus VARCHAR(255),
	engBall100 REAL,
	engBall12 REAL,
	engDPALevel VARCHAR(255),
	engBall	REAL,
	engPTName VARCHAR(255),
	engPTRegName VARCHAR(255),
	engPTAreaName VARCHAR(255),
	engPTTerName VARCHAR(255)
);
ALTER TABLE Eng ADD CONSTRAINT Eng_pk PRIMARY KEY (OUTID, engTest);

ALTER TABLE Eng
    ADD CONSTRAINT Eng_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Fra (
	OUTID VARCHAR(50),
	fraTest VARCHAR(255),
	fraTestStatus VARCHAR(255),
	fraBall100 REAL,
	fraBall12 REAL,
	fraDPALevel VARCHAR(255),
	fraBall	REAL,
	fraPTName VARCHAR(255),
	fraPTRegName VARCHAR(255),
	fraPTAreaName VARCHAR(255),
	fraPTTerName VARCHAR(255)
);
ALTER TABLE Fra ADD CONSTRAINT Fra_pk PRIMARY KEY (OUTID, fraTest);

ALTER TABLE Fra
    ADD CONSTRAINT Fra_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Deu (
	OUTID VARCHAR(50),
	deuTest	VARCHAR(255),
	deuTestStatus VARCHAR(255),
	deuBall100 REAL,
	deuBall12 REAL,
	deuDPALevel VARCHAR(255),
	deuBall	REAL,
	deuPTName VARCHAR(255),
	deuPTRegName VARCHAR(255),
	deuPTAreaName VARCHAR(255),
	deuPTTerName VARCHAR(255)
);
ALTER TABLE Deu ADD CONSTRAINT Deu_pk PRIMARY KEY (OUTID, deuTest);

ALTER TABLE Deu
    ADD CONSTRAINT Deu_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);


CREATE TABLE Spa (
	OUTID VARCHAR(50),
	spaTest	VARCHAR(255),
	spaTestStatus VARCHAR(255),
	spaBall100 REAL,
	spaBall12 REAL,
	spaDPALevel VARCHAR(255),
	spaBall	REAL,
	spaPTName VARCHAR(255),
	spaPTRegName VARCHAR(255),
	spaPTAreaName VARCHAR(255),
	spaPTTerName VARCHAR(255)
);
ALTER TABLE Spa ADD CONSTRAINT Spa_pk PRIMARY KEY (OUTID, spaTest);

ALTER TABLE Spa
    ADD CONSTRAINT Spa_fk FOREIGN KEY (OUTID)
        REFERENCES Human (OUTID);