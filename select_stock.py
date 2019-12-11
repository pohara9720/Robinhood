import json
from scraper import scrape_stocks

# NOTE Only stocks with the following criteria should be considered
# 1) Very high volume so it can be trading and sold quickly and easily
# 2) Has a percentage change of 3% or higher
# 3) Has a price change of more than $1.50
# 4) Is between $5.00 and %50.00 (affordable)
def is_considerable(data):
    is_affordable = data['price'] >= 500 and data['price'] <= 5000 
    is_acceptable_dollar_change = data['dollar_change'] > 150
    is_acceptable_percent_change = data['percent_change'] > 6
    is_acceptable_volume = data['volume'] > 1000000
    return is_affordable and is_acceptable_dollar_change and is_acceptable_percent_change and is_acceptable_volume

def select_stock(data):
    stocks_to_use = []
    considerable_stocks = list(filter(is_considerable, data))
    for stock in considerable_stocks:
        stocks_to_use.append(stock['symbol'])
    return stocks_to_use
    

