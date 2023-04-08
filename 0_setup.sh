#!/bin/bash

sudo apt update
sudo apt upgrade -y

# install apache2
sudo apt install apache2 -y

# install mysql
sudo apt install mariadb-server

# install pip
sudo apt install python3-pip -y

# install mysql-connector
pip install mysql-connector-python
# install openpyxl for access to xlsx for pandas
pip install openpyxl

# install google api magics 
sudo apt install python3-lxml -y
pip install yfinance

# install Flask
pip install Flask
# install mod_wsgi for running python web apps
sudo apt-get install libapache2-mod-wsgi-py3
# install python virtual environment
sudo apt-get install python3-venv -y
# create virtual environment
python3 -m venv myenv
