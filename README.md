# Robinhood

### Run virtual environment

###### This package must run inside a virtual env to create and activate the virtual environment run the following commands

`python3 -m venv robinhood-env`

`source robinhood-env/bin/activate`

###### Add this alias to create and activate python virtual-env in the future

`alias pv='f() { python3 -m venv $1-env && source $1-env/bin/activate};f'`

###### Use like so

`pv ENV_NAME`

### Installing dependencies

###### python stores its dependencies in a `requirements.txt` file. after creating your environment run the following command to install deps.

`pip install -r requirements.txt`

###### if you install additional packages use this command to save the new package to the `requirements.txt` file

`pip freeze > requirements.txt`

### Running script

###### After the virtual env is running and packages are installed run the following command to run the script

`python3 bot.py`

### Goal

1. Scrape the web for stocks and save it to a json file for viewing `scraper.py`
2. Filter the data and select stock or stocks that meet the criteria
3. Integrate with `robin_stocks` to get graph data and calculate when to buy and sell _TO BE IMPLEMENTED_
4. Integrate with `robin_stocks` api to buy and sell the stocks _TO BE IMPLEMENTED_
5. Create kron jobs for when to run the script _TO BE IMPLEMENTED_
