import mysql.connector
from datetime import date

# define the MySQL connection details
host = 'localhost'
database = 'dividendchampions'
user = 'access'
password = 'yellowrandomkittenporter'

def checkStockSymbol(stockSymbol):
    if stockSymbol == "ARTN.A":
        newSymbol = "ARTNA"
    elif stockSymbol == "BF.B":
        newSymbol = "BF-B"
    elif stockSymbol == "MKC.V":
        newSymbol = "MKC-V"
    elif stockSymbol == "RBCA.A":
        newSymbol = "RBCAA"
    else:
        newSymbol = stockSymbol
    return newSymbol

def setChampionsListToFalse():
    # set currentlyOnList in championsList to FALSE for all rows.
    query = "UPDATE championsList SET currentlyOnList = 0"
    runUpdate(query)
    return

def getStockInfoData():
    query = "SELECT id, symbol FROM stockInfo"
    results = runSelect(query)
    return results

def searchForSymbol(symbolToFind):
    symbolToFind = checkStockSymbol(symbolToFind)
    query = "SELECT * FROM stockInfo WHERE symbol = %s"
    data = (symbolToFind,)
    results = runSelectWithData(query, data)
    #results = runSelect(query)
    if results is None or len(results) == 0:
        returnValue = False
    else:
        returnValue = True
    return returnValue 

def createNewStockInfo(stockSymbol, stockCompany, stockSector, stockIndustry):
    stockSymbol = checkStockSymbol(stockSymbol)
    query = "INSERT INTO stockInfo (name, symbol, sector, industry) VALUES (%s, %s, %s, %s)"
    data = (stockCompany, stockSymbol, stockSector, stockIndustry)
    runInsert(query, data)

def addToChampionsList(stockSymbol, yearsOnList):
    query = "INSERT INTO championsList(stockInfoID, lastSeenOnList, currentlyOnList, yearsOn) VALUES (%s, %s, %s, %s)"
    tempResult = getStockInfoID(stockSymbol)
    today = date.today()
    data = (tempResult, today, True, yearsOnList)
    runInsert(query, data)

def updateChampionsList(stockSymbol, yearsOnList):
    query = "UPDATE championsList SET lastSeenOnList = %s, currentlyOnList = %s, yearsOn = %s WHERE stockInfoID = %s"
    tempResult = getStockInfoID(stockSymbol)
    today = date.today()
    data = (today, True, yearsOnList, tempResult)
    runUpdateWithData(query, data)

def putStockValuations(stockInfoID, sharePrice):
    query = "INSERT INTO currentValuations(stockInfoID, valuationDate, sharePrice) VALUES (%s, %s, %s)"
    today = date.today()
    data = (stockInfoID, today, sharePrice)
    runInsert(query, data)

#def putStockValuations(stockInfoID, sharePrice, pe):
#    query = "INSERT INTO currentValuations(stockInfoID, valuationDate, sharePrice, pe) VALUES (%s, %s, %s, %s)"
#    today = date.today()
#    data = (stockInfoID, today, sharePrice, pe)
#    runInsert(query, data)

def getStockInfoID(stockSymbol):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    stockSymbol = checkStockSymbol(stockSymbol)
    query = "SELECT id FROM stockInfo WHERE symbol = %s"
    cursor.execute(query, (stockSymbol,))
    #this is complete cause of this fetchone...
    row = cursor.fetchone()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    if row is None:
        returnValue = False
    else:
        returnValue = row[0] 
    return returnValue

def truncateValuations():
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    truncate_query = "TRUNCATE currentValuations"
    cursor.execute(truncate_query)
    # Commit the changes to the database
    cnx.commit()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()

def runSelect(tmpQuery):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    #execute the query
    cursor.execute(tmpQuery)
    results = cursor.fetchall()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    if results is None or len(results) == 0:
        return
    return results

def runSelectWithData(tmpQuery, tmpData):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    #execute the query
    cursor.execute(tmpQuery, tmpData)
    results = cursor.fetchall()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    if results is None or len(results) == 0:
        return
    return results

def runUpdate(tmpQuery):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    # execute the query
    cursor.execute(tmpQuery)
    cnx.commit()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()

def runUpdateWithData(tmpQuery, tmpData):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    # execute the query
    cursor.execute(tmpQuery, tmpData)
    cnx.commit()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    
def runInsert(tmpQuery, tmpData):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    #execute the query
    cursor.execute(tmpQuery, tmpData)
    cnx.commit()
    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
