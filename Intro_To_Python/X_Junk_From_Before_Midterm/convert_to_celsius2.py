def convert_to_celsius(fahrenheit, degrees): 
    """ (number, int) -> float  # much better 
 
    Return the number of Celsius degrees equivalent to fahrenheit degrees. 
    With n decimal places, where n is the number of degrees of freedom.
 
    >>> convert_to_celsius(75, 5) 
    23.88889
    >>> convert_to_celsius(75, 4)
    23.8889
    >>> convert_to_celsius(65, 5)
    18.33333
    """
    return round((fahrenheit - 32.0) * 5.0 / 9.0, degrees)
