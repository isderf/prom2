from dao.dao import runSelect

def getAllStockInfo():
    query = ("SELECT id, name, symbol FROM stockInfo")
    stock_info = runSelect(query)
    return stock_info
