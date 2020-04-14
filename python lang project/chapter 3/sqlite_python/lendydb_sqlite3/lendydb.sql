PRAGMA Foreign_Keys=True;


drop table loan;
drop table item;
drop table member;

create table member (
ID INT PRIMARY KEY,
Name TEXT NOT NULL,
Email TEXT);

create table item (
ID INT PRIMARY KEY,
Name TEXT NOT NULL,
Description TEXT NOT NULL,
OwnerID INTEGER NOT NULL REFERENCES member(ROWID),
Price NUMERIC,
Condition TEXT,
DateRegistered TEXT);

create table loan (
ID INT PRIMARY KEY,
ItemID INTEGER NOT NULL REFERENCES item(ROWID),
BorrowerID INTEGER NOT NULL REFERENCES member(ROWID),
DateBorrowed TEXT NOT NULL,
DateReturned TEXT);
