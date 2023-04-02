# prom2
cause FIRE wasn't cool enough

Stock
  ID - PK
  Name (text)
  Symbol (text)
  Sector (text)
  Industry (text)
 
ChampionsList
  ID - PK
  Stock_ID
  LastSeenOnList (date)
  CurrentlyOnList (bool)
  YearsOn (int)
  
CurrentValuations
  Stock_ID
  Date (date)
  SharePrice (float)
  PE (float)
  
Holdings
  ID - PK
  Stock_ID
  DateBought (date)
  PricePaid (float)
  Quantity (int)
  
Dividends
  ID - PK
  Stock_ID
  DatePaid (date)
  Amount (float)
