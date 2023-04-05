import mysql.connector
from datetime import date

# define the MySQL connection details
host = 'localhost'
database = 'dividendchampions'
user = 'access'
password = 'yellowrandomkittenporter'

def setChampionsListToFalse():
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()

    # set currentlyOnList in championsList to FALSE for all rows.
    query = "UPDATE championsList SET currentlyOnList = 0"

    # execute the query
    cursor.execute(query)
    cnx.commit()

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return

def getStockInfoData():
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    query = "SELECT id, symbol FROM stockInfo"

    #execute the query
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) == 0:
        return
    
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return results

def searchForSymbol(symbolToFind):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    query = "SELECT * FROM stockInfo WHERE symbol = %s"

    #execute the query
    cursor.execute(query, (symbolToFind,))
    results = cursor.fetchall()
    if len(results) == 0:
        returnValue = False
    else:
        returnValue = True
    
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return returnValue 

def createNewStockInfo(stockSymbol, stockCompany, stockSector, stockIndustry):
    #'Symbol', 'Company', 'Sector', 'Industry'
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    query = "INSERT INTO stockInfo (name, symbol, sector, industry) VALUES (%s, %s, %s, %s)"
    data = (stockCompany, stockSymbol, stockSector, stockIndustry)

    #execute the query
    cursor.execute(query, data)
    cnx.commit()

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return 

def getStockInfoID(stockSymbol):
    #stockInfoID, lastSeenOnList, currentlyOnList, yearsOn
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    query = "SELECT id FROM stockInfo WHERE symbol = %s"

    cursor.execute(query, (stockSymbol,))
    row = cursor.fetchone()
    if row is None:
        returnValue = False
    else:
        returnValue = row[0] 

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return returnValue

def addToChampionsList(stockSymbol, yearsOnList):
    #stockInfoID, lastSeenOnList, currentlyOnList, yearsOn
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()

    tempResult = getStockInfoID(stockSymbol)

    query = "INSERT INTO championsList(stockInfoID, lastSeenOnList, currentlyOnList, yearsOn) VALUES (%s, %s, %s, %s)"
    today = date.today()
    data = (tempResult, today, True, yearsOnList)

    #execute the query
    cursor.execute(query, data)
    cnx.commit()

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()

def updateChampionsList(yearsOnList):
    #stockInfoID, lastSeenOnList, currentlyOnList, yearsOn
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()

    tempResult = getStockInfoID(stockSymbol)

    # set currentlyOnList in championsList to FALSE for all rows.
    query = "UPDATE championsList SET lastSeenOnList = %s, currentlyOnList = %s, yearsOn = %s WHERE stockInfoID = %s"
    today = date.today()
    data = (today, True, yearsOnList, tempResult)

    #execute the query
    cursor.execute(query, data)
    cnx.commit()

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
