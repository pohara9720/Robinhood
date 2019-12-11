import json
from select_stock import select_stock

with open('stock_data.json') as json_file:
    data = json.load(json_file)
    stock_data = data['stocks']
    stocks_to_use = select_stock(stock_data)
    print(stocks_to_use)