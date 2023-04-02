-- Run this to secure the server first time
-- sudo mysql_secure_installation

-- To setup db from script
-- sudo mysql < /home/ubuntu/RaspberryPiScripts/Setup/ServerSetup.sql

CREATE database dividendchampions;
use dividendchampions;
CREATE USER 'readwrite'@'localhost' IDENTIFIED BY 'yellowrandomkittenporter';
GRANT ALL PRIVILEGES ON dividendchampions.* TO 'readwrite'@'localhost';

flush PRIVILEGES;

CREATE TABLE stockInfo(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	symbol VARCHAR(5) NOT NULL,
	sector VARCHAR(50),
	industry VARCHAR(50),
	PRIMARY KEY ( id )
);

CREATE TABLE championsList(
	id INT NOT NULL AUTO_INCREMENT,
	stockInfoID INT,
	lastSeenOnList DATE, 
	currentlyOnList TINYINT(1),
	yearsOn TINYINT(4),
	PRIMARY KEY ( id ),
	FOREIGN KEY ( stockInfoID ) REFERENCES stockInfo( id )
);

CREATE TABLE currentValuations(
	stockInfoID INT,
	valuationDate DATE,
	sharePrice FLOAT,
	pe FLOAT
);

CREATE TABLE holdings(
	id INT NOT NULL AUTO_INCREMENT,
	stockInfoID INT,
	dateBought DATE,
	pricePaid FLOAT,
	quantity INT,
	PRIMARY KEY ( id ),
	FOREIGN KEY ( stockInfoID ) REFERENCES stockInfo( id )
);

CREATE TABLE dividends(
	id INT NOT NULL AUTO_INCREMENT,
	stockInfoID INT,
	datePaid DATE,
	amount FLOAT,
	PRIMARY KEY ( id ),
	FOREIGN KEY ( stockInfoID ) REFERENCES stockInfo( id )
);

show tables;
-- this section only displays for the admin
-- show databases;
-- select user from mysql.user;
-- show grants for readonly@localhost;
-- show grants for readwrite@localhost;
-- show grants for program@localhost;
-- show tables;
-- describe stockdates;
-- describe stockinfo;


-- TODO create users and grants
-- creates users
-- create user 'readonly'@'localhost';
-- create user 'readwrite'@'localhost';
-- create user 'program'@'localhost';

-- grants the new users their permissions
-- grant Update,Insert,Select,Delete on dividendchampions.* to 'readwrite'@'localhost';
-- grant Update,Insert,Select,Grant Option,Create on dividendchampions.* to 'program'@'localhost';
