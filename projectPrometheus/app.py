from flask import Flask, render_template, request
from blueprints.valuations_bp import valuations_bp
import mysql.connector

app = Flask(__name__)

app.register_blueprint(valuations_bp)

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
        stock_id = request.form.get('stock_name')
        date_bought = request.form.get('date_bought')
        price_paid = float(request.form.get('price_paid'))
        quantity = int(request.form.get('quantity'))

        # Store the holdings data in the database
        # establish a connection to the database
        cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')
        # create a cursor object to execute SQL queries
        cursor = cnx.cursor()
    
        query = "INSERT INTO holdings (stockInfoID, dateBought, pricePaid, quantity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (stock_id, date_bought, price_paid, quantity))
        cnx.commit()
    if request.method == 'GET':
        # establish a connection to the database
        cnx = mysql.connector.connect(user='access', password='yellowrandomkittenporter', host='localhost', database='dividendchampions')
        # create a cursor object to execute SQL queries
        cursor = cnx.cursor()

    # Retrieve the holdings data from the database
    #query = "SELECT * FROM holdings"
    query = "SELECT holdings.*, stockInfo.name FROM holdings INNER JOIN stockInfo ON holdings.stockInfoID = stockInfo.id"
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('holdings.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
