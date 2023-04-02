#!/bin/bash

sudo apt update
sudo apt upgrade -y

#install apache2
sudo apt install apache2 -y

#install mysql
sudo apt install mariadb-server

#install pip
sudo apt install python3-pip -y

#install mysql-connector
pip install mysql-connector-python
#install openpyxl for access to xlsx for pandas
pip install openpyxl
