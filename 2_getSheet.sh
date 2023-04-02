#!/bin/bash
#Go and get the Dividend Champions xlsx
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1D4H2OoHOFVPmCoyKBVCjxIl0Bt3RLYSz' -O USDividendChampions.xlsx

#del the old old spreadsheet
rm spreadsheet/USDividendChampions.old

#move the old spreadsheet
mv spreadsheet/USDividendChampions.xlsx spreadsheet/USDividendChampions.old

#move it to a .xlsx file ending
mv USDividendChampions.xlsx spreadsheet/USDividendChampions.xlsx
