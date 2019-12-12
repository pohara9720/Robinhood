from bs4 import BeautifulSoup
import requests
import json 
from helpers import convert_price,convert_volume,convert_percentage

yahoo_finance_url = 'https://finance.yahoo.com/gainers'
yahoo_finance_response = requests.get(yahoo_finance_url,timeout=5)
yahoo_finance_soup = BeautifulSoup(yahoo_finance_response.text,"html.parser")

fear_greed_url = 'https://money.cnn.com/data/fear-and-greed/'
fear_greed_response = requests.get(fear_greed_url,timeout=5)
fear_greed_soup = BeautifulSoup(fear_greed_response.text,"html.parser")

## Data to be dumped in json file
data={}
data['stocks']=[]

class Stock:
    def __init__(self,symbol,name, price,dollar_change,percent_change,volume):
        self.name = name
        self.price = price
        self.symbol = symbol
        self.dollar_change = dollar_change
        self.percent_change = percent_change
        self.volume = volume

    def __repr__(self):
        return { 
            'symbol':self.symbol, 
            'name': self.name, 
            'price': self.price, 
            'dollar_change': self.dollar_change,
            'percent_change': self.percent_change,
            'volume': self.volume 
        }

# Scrape yahoo finance for up to date stocks
def scrape_stocks():
    # Get all table rows from soup scrape
    table_rows = yahoo_finance_soup.find_all('tr',{'class':'simpTblRow'})

    # Get all table data from soup scrape
    for row in table_rows:
        symbol = row.find('td', {'aria-label': 'Symbol'}).a.text
        name = row.find('td', {'aria-label': 'Name'}).text
        price_text = row.find('td',{'aria-label':'Price (Intraday)'}).span.text
        price = convert_price(price_text) # Convert price to workable integer
        dollar_change_text = row.find('td', {'aria-label': 'Change'}).span.text
        dollar_change = convert_price(dollar_change_text) # Convert dollar change to workable integer
        percent_change_text = row.find('td', {'aria-label': '% Change'}).span.text
        percent_change = convert_percentage(percent_change_text) # Convert percentage change to workable integer
        volume_text = row.find('td', {'aria-label': 'Volume'}).span.text
        volume = convert_volume(volume_text) # Convert volume to workable integer
        # Create new object
        stock_data = Stock(symbol,name,price,dollar_change,percent_change,volume)
        # Append to data object
        data['stocks'].append(stock_data.__repr__())
    #Write data to file to view
    with open('stock_data.json', 'w') as f:
        json.dump(data,f,indent=2,sort_keys=True)

# Scrape the fear greed index
def scrape_fear_greed_index():
    div = fear_greed_soup.find_all(id='needleChart')
    div = str(div[0])
    position = div.find('Fear &amp; Greed Now: ')
    position = position + len('Fear &amp; Greed Now: ')
    current_index = int(div[position:position+3].strip())
    #Append to data object
    data['fear_greed_index'] = current_index

    #Write data to file to view
    with open('stock_data.json', 'w') as f:
        json.dump(data,f,indent=2,sort_keys=True)
