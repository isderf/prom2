import csv
import mysql.connector
import projectPrometheus.dao.dao as dao

# Define the file path of the CSV file
csv_file_path = 'holdings.csv'  # Change to the actual path of your CSV file

# Open the CSV file for reading
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Extract data from the row
        date_bought, price_paid, quantity, stock_symbol = row

        stockSymbolID = dao.getStockInfoID(stock_symbol)
        tmpData = (stockSymbolID, date_bought, price_paid, quantity)
        query = "INSERT INTO holdings (stockInfoID, dateBought, pricePaid, quantity) VALUES (%s, %s, %s, %s)"
        dao.runInsert(query, tmpData)

print("Data has been successfully imported into the database.")
