import mysql.connector
import csv
import projectPrometheus.dao.dao as dao

# Define your SQL query
query = """
    SELECT h.dateBought, h.pricePaid, h.quantity, stockInfo.symbol AS stockSymbol
    FROM holdings AS h
    JOIN stockInfo ON h.stockInfoID = stockInfo.id;
"""

# Execute the query using the runSelect function
results = dao.runSelect(query)

# Define the file path where you want to save the results
file_path = 'holdings.csv'

# Open the file in write mode with a comma as the delimiter
with open(file_path, 'w', newline='') as file:
    # Use a comma as the delimiter
    delimiter = ','

    # Create a CSV writer object
    csv_writer = csv.writer(file, delimiter=delimiter)

    # Write the header
    csv_writer.writerow(["DateBought", "PricePaid", "Quantity", "StockSymbol"])

    # Write each row of the result
    for row in results:
        csv_writer.writerow(row)

print(f"Results have been saved to {file_path}")
