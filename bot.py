import json
from select_stock import select_stock
from scraper import scrape_stocks




##Generate array of stocks that meet critieria to trade today
def pick_stocks_for_today():
    ## Array of stocks to populate
    todays_stocks = []
    ## Scrape the web for stocks
    scrape_stocks()

    with open('stock_data.json') as json_file:
        data = json.load(json_file)
        stock_data = data['stocks']
        selected_stocks = select_stock(stock_data)
        for stock in selected_stocks:
            todays_stocks.append(stock)
        return todays_stocks

        

stocks = pick_stocks_for_today()

print('Todays stocks chosen are: ', stocks)