import dao
import time
import yfinance as yf

# for loop through each row in stockInfo
loopVariable = dao.getStockInfoData()

# query google for sharePrice and pe
for row in loopVariable:
    # get sharePrice from google
    # Create a ticker object for Google
    goog = yf.Ticker(row[1])
    ##### do something with row[1]
    # Get the current stock price
    current_price = goog.info['regularMarketPrice']
    # get pe from google
    pe_ratio = goog.info['trailingPE']

    print("Ticker: ", row[1])
    print("Current Stock Price: $", current_price)
    print("PE Ratio: ", pe_ratio)

    time.sleep(2)
    # store in currentValuations
    #dao.putStockValuations(sharePrice, pe)
