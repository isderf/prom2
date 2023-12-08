import projectPrometheus.dao.dao as dao
import time
import yfinance as yf

# for loop through each row in stockInfo
loopVariable = dao.getStockInfoData()

#truncate table
dao.truncateValuations()

# query google for sharePrice and pe
for row in loopVariable:
    stockSymbol = row[1]
    # get sharePrice from google
    # Create a ticker object for Google
    goog = yf.Ticker(stockSymbol)

    # Get the current stock price
    current_price = goog.info['currentPrice']
    # get pe from google
    if "trailingPE" in goog.info:
        pe_ratio = goog.info['trailingPE']
    else:
        pe_ratio = None 
        print("PE error for: ", stockSymbol)
    
    #goog = yf.download(stockSymbol, period = '1d')
    ##infoTemp = goog.get_info()
    #print(goog)
    #print('*'*20)
    
    ## Get the current stock price
    #current_price= goog['Open'][0]

    print("Ticker: ", stockSymbol)
    print("Current Stock Price: $", current_price)
    print("PE Ratio: ", pe_ratio)

    time.sleep(1)
    # store in currentValuations
    dao.putStockValuations(row[0], current_price, pe_ratio)
    #dao.putStockValuations(row[0], current_price)
