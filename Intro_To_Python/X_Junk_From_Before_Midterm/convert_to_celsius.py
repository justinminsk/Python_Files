
def convert_to_celsius(fahrenheit): 
    """ (number) -> string  # hmmm 
 
    Return the number of Celsius degrees equivalent to fahrenheit degrees. 
    with 1 decimal place 
 
    >>> convert_to_celsius(75) 
    '23.9' 
    """ 
    return float(format((fahrenheit - 32.0) * 5.0 / 9.0, '.1f'))
