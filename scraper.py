from bs4 import BeautifulSoup
import requests
import json 

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


table_rows = soup.find_all('tr',{'class':'simpTblRow'})

for row in table_rows:
    symbol = row.find('td', {'aria-label': 'Symbol'}).a.text
    name = row.find('td', {'aria-label': 'Name'}).text
    price = row.find('td',{'aria-label':'Price (Intraday)'}).span.text
    dollar_change = row.find('td', {'aria-label': 'Change'}).span.text
    percent_change = row.find('td', {'aria-label': '% Change'}).span.text
    volume = row.find('td', {'aria-label': 'Volume'}).span.text
    # Create new object
    stock_data = Stock(symbol,name,price,dollar_change,percent_change,volume)
    # Append to data object
    data['stocks'].append(stock_data.__repr__())


with open('stock-data.json', 'w') as f:
    for stock in data['stocks']:
        json.dump(stock,f,indent=2,sort_keys=True)