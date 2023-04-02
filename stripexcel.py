import openpyxl
import pandas as pd
import mysql.connector
import dao

# define the MySQL connection details
host = 'localhost'
database = 'dividendchampions'
user = 'access'
password = 'yellowrandomkittenporter'

# define the columns we want
sheet_name = 'Champions'
columns = ['Symbol', 'Company', 'Sector', 'No Years', 'Industry']

dao.setChampionsListToFalse()

# grab the data
df = pd.read_excel('spreadsheet/USDividendChampions.xlsx', sheet_name=sheet_name, usecols=columns, skiprows=2)

# iterate over the rows of the DataFrame and insert them into the MySQL table
for row in df.itertuples():
    # If Symbol doesn't exist in db, create new stockInfo
    if not dao.searchForSymbol(row[1]):
        dao.createNewStockInfo(row[1], row[2], row[3], row[5])
        #   AND add to championsList
        # dao.addToChampionsList(
# Else update championsList with new lastSeenOn, currentlyOnList, yearsOn
