from flask import Blueprint

valuations_bp = Blueprint('valuations', __name__)

@valuations_bp.route('/valuations')
def valuations():
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
