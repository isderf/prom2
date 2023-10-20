from dao.dao import runSelectWithData

def getStockDataBySector():
    # Query to get Stock Sectors
    query = ("SELECT DISTINCT sector FROM stockInfo")
    sectors = runSelectWithData(query, ())
    
    # Dictionary to store stock data by sector
    data = { 'totalValue': 0, 'sectors': {}}
    
    for sector in sectors:
        sectorName = sector[0]
        addSector(data, sectorName)

    # Query to retrieve stock data grouped by sector
    query2 = ("SELECT s.sector, s.symbol, s.name, v.sharePrice, h.quantity "
             "FROM stockInfo s "
             "JOIN currentValuations v ON s.id = v.stockInfoID "
             "JOIN holdings h ON s.id = h.stockInfoID "
             "WHERE h.quantity > 0")

    # Execute the query and retrieve the results
    results = runSelectWithData(query2, ())

    # Process the results and group by sector
    for (sector, symbol, stockName, sharePrice, quantity) in results:
        stock_value = quantity * sharePrice
        addStock(data, sector, symbol, stockName, quantity, sharePrice, stock_value)

    #Iterate over all the sectors
    totalValue = data['totalValue']
    for sector in sectors:
        sectorName = sector[0]
        totalSectorValue = 0.0

        # Calculate the total value for the current sector
        for stock in data['sectors'][sectorName]['stocks']:
            stockValue = stock['value']
            totalSectorValue += stockValue
            totalValue += stockValue

        # Update the sector's value 
        data['sectors'][sectorName]['value'] = totalSectorValue
        data['totalValue'] = totalValue

    # calculate the % value for each sector
    for sector in sectors:
        sectorName = sector[0]
        sectorTmp = data['sectors'][sectorName]['value']
        totalTmp = data['totalValue']
        if totalTmp > 0:
            data['sectors'][sectorName]['percent'] = (sectorTmp / totalTmp) * 100
        else:
            data['sectors'][sectorName]['percent'] = 0

    # Sort sectors by percent from lowest to highest
    sorted_sectors = sorted(sectors, key=lambda sector: data['sectors'][sector[0]]['percent'])

    # Reconstruct the data dictionary with sorted sectors
    sorted_data = {
        'totalValue': data['totalValue'],
        'sectors': {sector[0]: data['sectors'][sector[0]] for sector in sorted_sectors}
    }

    return sorted_data

def addStock(data, sector_name, symbol, stock_name, stock_quantity, stock_shareprice, stock_value):
    sector = data['sectors'].get(sector_name)
    if sector is None:
        add_sector(data, sector_name)
        sector = data['sectors'][sector_name]

    stock_exists = False
    for stock in sector['stocks']:
        if stock['symbol'] == symbol:
            stock_exists = True
            stock['name'] = stock_name
            stock['quantity'] += stock_quantity
            stock['shareprice'] = stock_shareprice
            stock['value'] += stock_value
            break

    if not stock_exists:
        sector['stocks'].append({
            'symbol': symbol,
            'name': stock_name,
            'quantity': stock_quantity,
            'shareprice': stock_shareprice,
            'value': stock_value
        })

    sector['value'] += stock_value

def addSector(data, sectorName):
        data['sectors'][sectorName] = { 'stocks': [], 'value': 0.0, 'percent': 0.0 }
