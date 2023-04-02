-- Run this to secure the server first time
-- sudo mysql_secure_installation


-- sudo mysql < /home/ubuntu/RaspberryPiScripts/Setup/ServerSetup.sql to run

CREATE database dividendchampions;

flush PRIVILEGES;
SET password FOR 'root'@'localhost' = 'blueberry';
use mysql;
CREATE USER 'user'@'localhost' identified BY 'blueberry';
use dividendchampions;
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';

use dividendchampions;
CREATE TABLE stockdates(dateofinfo date, yearsonlist int(100));
CREATE TABLE stockinfo(stickersymbol varchar(30), stockname varchar(60), sector varchar(60), industry varchar(60));
CREATE TABLE graphdata(ticker varchar(10), name varchar(90), currentprice varchar(60), forwardPE varchar(60), sector varchar(60), curDate date);

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
