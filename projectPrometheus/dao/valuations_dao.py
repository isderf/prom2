from dao.dao import runSelectWithData

def getCurrentValutionsBySector():
    # execute a query to get current valuations by sector
    query = ("SELECT s.sector, s.name, s.symbol, v.sharePrice, v.pe, SUM(h.quantity) as quantity "
             "FROM currentValuations v "
             "JOIN stockInfo s ON v.stockInfoID = s.id "
             "LEFT JOIN holdings h ON v.stockInfoID = h.stockInfoID "
             "GROUP BY s.sector, s.name, s.symbol, v.sharePrice, v.pe "
             "ORDER BY s.sector, v.pe ASC")
    #query = ("SELECT s.sector, s.name, s.symbol, v.sharePrice, v.pe, h.quantity "
    #         "FROM currentValuations v "
    #         "JOIN stockInfo s ON v.stockInfoID = s.id "
    #         "LEFT JOIN holdings h ON v.stockInfoID = h.stockInfoID "
    #         "ORDER BY s.sector, v.pe ASC")
    results = runSelectWithData(query, ())

    # process the results and group by sector
    grouped_results = {}
    for (sector, name, symbol, share_price, pe, quantity) in results:
        if sector not in grouped_results:
            grouped_results[sector] = []
        grouped_results[sector].append({'name': name, 'symbol': symbol, 'share_price': share_price, 'pe': pe, 'quantity': quantity})

    return grouped_results
