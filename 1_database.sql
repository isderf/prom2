-- Run this to secure the server first time
-- sudo mysql_secure_installation

-- To setup db from script
-- sudo mysql < 1_database.sql

CREATE database dividendchampions;
use dividendchampions;
CREATE USER 'access'@'localhost' IDENTIFIED BY 'yellowrandomkittenporter';
GRANT ALL PRIVILEGES ON dividendchampions.* TO 'access'@'localhost';

flush PRIVILEGES;

CREATE TABLE stockInfo(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	symbol VARCHAR(6) NOT NULL,
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
