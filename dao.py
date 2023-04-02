import mysql.connector

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

def searchForSymbol(symbolToFind):
    cnx = mysql.connector.connect(host=host, database=database, user=user, password=password)
    cursor = cnx.cursor()
    # set currentlyOnList in championsList to FALSE for all rows.
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
    # set currentlyOnList in championsList to FALSE for all rows.
    print("Name: " + stockCompany + " Symbol: " + stockSymbol + " Sector: " + stockSector + " Industry: " + stockIndustry)
    query = "INSERT INTO stockInfo (name, symbol, sector, industry) VALUES (%s, %s, %s, %s)"
    data = (stockCompany, stockSymbol, stockSector, stockIndustry)

    #execute the query
    cursor.execute(query, data)
    cnx.commit()

    # close the cursor and MySQL connection
    cursor.close()
    cnx.close()
    return 