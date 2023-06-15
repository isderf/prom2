from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# @app.route('/', methods=['GET'])

@app.route('/addHolding', methods=['GET'])
def holdings_form():
    # establish a connection to the database
    cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')

    # create a cursor object to execute SQL queries
    cursor = cnx.cursor()
    
    cursor.execute("SELECT id, name, symbol FROM stockInfo")
    stock_info = cursor.fetchall()
    return render_template('holdings_form.html', stock_info=stock_info)


# Define a route to process the form submission and display the holdings
@app.route('/viewHoldings', methods=['GET', 'POST'])
def display_holdings():
    if request.method == 'POST':
        stock_name = request.form.get('stock_name')
        date_bought = request.form.get('date_bought')
        price_paid = float(request.form.get('price_paid'))
        quantity = int(request.form.get('quantity'))

        # Store the holdings data in the database
        # establish a connection to the database
        cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')
        # create a cursor object to execute SQL queries
        cursor = cnx.cursor()
    
        query = "INSERT INTO holdings (stockInfoID, dateBought, pricePaid, quantity) VALUES (%s, %s, %s, %s)"
## TODO get stockInfoID
        cursor.execute(query, (stock_name, date_bought, price_paid, quantity))
        cnx.commit()
    if request.method == 'GET':
        # establish a connection to the database
        cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')
        # create a cursor object to execute SQL queries
        cursor = cnx.cursor()

    # Retrieve the holdings data from the database
    query = "SELECT * FROM holdings"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('holdings.html', data=data)

@app.route('/valuations')
def index():
    # establish a connection to the database
    cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')

    # create a cursor object to execute SQL queries
    cursor = cnx.cursor()

    # execute a query to get current valuations by sector
    query = ("SELECT s.sector, s.name, s.symbol, v.sharePrice, v.pe "
             "FROM currentValuations v "
             "JOIN stockInfo s ON v.stockInfoID = s.id "
             "ORDER BY s.sector, v.pe ASC")
    cursor.execute(query)

    # process the results and group by sector
    results = {}
    for (sector, name, symbol, share_price, pe) in cursor:
        if sector not in results:
            results[sector] = []
        results[sector].append({'name': name, 'symbol': symbol, 'share_price': share_price, 'pe': pe})

    # close the cursor and connection
    cursor.close()
    cnx.close()

    # render the template with the results
    return render_template('valuations.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
