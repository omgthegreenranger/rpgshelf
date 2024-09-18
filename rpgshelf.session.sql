CREATE TABLE system(
    system_name text,
    altname text,
    altname2 text,
    rid int,
    lsid int uniqueidentifier,
    system text,
    description text,
    image text,
    thumbnail text
    );

CREATE TABLE library(
    lsid int,
    bid uniqueidentifier,
    rbid int,
    title text,
    publishers array,
    series text,
    publisher blob,
    designers blob,
    artists blob,
    producers blob,
    year int,
    description text,
    image text,
    thumbnail text,
    FOREIGN KEY(lsid) REFERENCES system(lsid)
    );

-- DROP TABLE library;