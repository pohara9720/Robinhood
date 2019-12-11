from bs4 import BeautifulSoup
import requests
import json 
from helpers import convert_price,convert_volume,convert_percentage

url = 'https://finance.yahoo.com/gainers'
response = requests.get(url,timeout=5)
soup = BeautifulSoup(response.text,"html.parser")

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

# Get all table rows from soup scrape
table_rows = soup.find_all('tr',{'class':'simpTblRow'})

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