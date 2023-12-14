-- CREATE TABLE games(
--     gid uniqueidentifier, 
--     name varchar(255), 
--     rid int, 
--     system varchar(255), 
--     rules varchar(255),
--     description text,
--     publisher varchar(255), 
--     year YEAR)

CREATE TABLE library(
    gid int, 
    bid uniqueidentifier,
    brid int,
    type varchar(255),
    description text,
    path varchar,
    image text
    )