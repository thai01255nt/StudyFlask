DROP TABLE  if EXISTS flask_study;
CREATE TABLE flask_study (
    id integer primary key autoincrement,
    title text not null,
    'text' text not null
);