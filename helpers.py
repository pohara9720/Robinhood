# Strip commas from price text and convert to number and return a price in pennies
def convert_price(text):
    removed_commas = text.replace(',','')
    to_float = float(removed_commas)
    return int(to_float * 100)

# Convert volume to workable integer
def convert_volume(volume_string):
    millions = volume_string.count('M') 
    remove_m = volume_string.replace('M','')
    remove_commas = remove_m.replace(',','')
    volume_float = float(remove_commas)
    if millions >= 1:
        return int(volume_float * 1000000)
    else:
        return int(volume_float)




    
    
    
