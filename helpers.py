# Strip commas from price text and convert to number and return a price in pennies
def convert_price(price_string):
    no_commas = price_string.replace(',','')
    no_plus = no_commas.replace('+','')
    to_float = float(no_plus)
    return int(to_float * 100)

# Convert volume to workable integer
def convert_volume(volume_string):
    millions = volume_string.count('M') 
    no_m = volume_string.replace('M','')
    no_commas = no_m.replace(',','')
    volume_float = float(no_commas)
    if millions >= 1:
        return int(volume_float * 1000000)
    else:
        return int(volume_float)

# Convert percentage to a workable integer
def convert_percentage(change_string):
    no_percent = change_string.replace('%','')
    no_plus = no_percent.replace('+','')
    return float(no_plus)

    
    
    
