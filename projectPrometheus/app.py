from flask import Flask, render_template, request
from dao import valuations_dao, holdings_dao
import mysql.connector

app = Flask(__name__)

# @app.route('/', methods=['GET'])

@app.route('/addHolding', methods=['GET'])
def addHolding():
    addHolding = holdings_dao.getAllStockInfo()
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

        data = (stock_id, date_bought, price_paid, quantity)
        holdings_dao.insertNewHolding(data)

    # Retrieve the holdings data from the database
    data = holdings_dao.showHoldings()
    return render_template('holdings.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
