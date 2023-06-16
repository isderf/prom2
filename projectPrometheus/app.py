from flask import Flask, render_template, request
from dao import valuations_dao, addHolding_dao, viewHoldings_dao
import mysql.connector

app = Flask(__name__)

# @app.route('/', methods=['GET'])

@app.route('/addHolding', methods=['GET'])
def addHolding():
    addHolding = addHolding_dao.getAllStockInfo()
    return render_template('addHolding_form.html', stock_info=addHolding)

@app.route('/valuations', methods=['GET'])
def valuations():
    valuations = valuations_dao.getCurrentValutionsBySector()
    return render_template('valuations.html', results=valuations)

# Define a route to process the form submission and display the holdings
@app.route('/viewHoldings', methods=['GET', 'POST'])
def viewHoldings():
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
