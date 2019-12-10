import math


# TODO remove trailing decimals from number
# Strip commas from price text and convert to number and return a price in pennies
def convert_price(text):
    removed_commas = text.replace(',','')
    to_float = float(removed_commas)
    return to_float * 100

#TODO need to convert volume to be a readable number with out M and K
# Convert volume to 
def convert_volume(price):
    print('to be implemented')
