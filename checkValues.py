import dao
import time
import yfinance as yf

# for loop through each row in stockInfo
loopVariable = dao.getStockInfoData()

# query google for sharePrice and pe
for row in loopVariable:
    stockSymbol = row[1]
    # get sharePrice from google
    # Create a ticker object for Google
    goog = yf.Ticker(stockSymbol)
    # Get the current stock price
    current_price = goog.info['regularMarketPrice']
    # get pe from google
    if "trailingPE" in goog.info:
        pe_ratio = goog.info['trailingPE']
    else:
        pe_ratio = None 
        print("PE error for: ", stockSymbol)

    print("Ticker: ", stockSymbol)
    print("Current Stock Price: $", current_price)
    print("PE Ratio: ", pe_ratio)

    time.sleep(1)
    # store in currentValuations
    dao.putStockValuations(row[0], current_price, pe_ratio)
