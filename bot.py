import json
from select_stock import select_stock

todays_stocks = []

with open('stock_data.json') as json_file:
    data = json.load(json_file)
    stock_data = data['stocks']
    selected_stocks = select_stock(stock_data)
    for stock in selected_stocks:
        todays_stocks.append(stock)

print('Todays stocks chosen are: ', todays_stocks)