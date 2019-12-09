# Robinhood

### Run virtual environment 
###### This package must run inside a virtual env to create and activate the virtual environment run the following commands

`python3 -m venv robinhood-env`

`source robinhood-env/bin/activate`

### Installing dependencies 
###### python stores its dependencies in a `requirements.txt` file. after creating your environment run the following command to install deps.

`pip install -r requirements.txt`

###### if you install additional packages use this command to save the new package to the `requirements.txt` file

`pip freeze > requirements.txt`

### Running script
###### After the virtual env is running and packages are installed run the following command to run the script

`python3 scraper.py`