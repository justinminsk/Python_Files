def convert_fuel(fuel, amount):
    """
    convert_fuel(str, number) -> float

    Take either mpg or liters per 100km and convert it to the other form. This means takes mpg and
    converts it to liters per 100km and vice versa.

    >>> convert_fuel('mpg', 45)
    6.277333333333334 liters per 100km
    
    >>> convert_fuel('liters per 100km', 5)
    47.0428 mpg

    >>> convert_fuel('liters per 100km', 2)
    117.607 mpg

    >>> convert_fuel('liters per 100km', 6)
    39.202333333333335 mpg

    >>> convert_fuel('mpg', 60)
    4.708 liters per 100km

    >>> convert_fuel('mpg', 15)
    18.832 liters per 100km

    >>> convert_fuel('mpg', 41)
    6.889756097560976 liters per 100km
    """
    boo = False
    if fuel == 'MPG' or fuel == 'mpg':
        amount = (282.48/amount)
        print(amount,'liters per 100km')
        boo = True
    elif fuel == 'liters per 100km' or fuel == 'liters per 100KM' or fuel == 'liters per 100Km':
        amount = (235.214/amount)
        print(amount,'mpg')
        boo = True
    elif boo == False:
        print('invalid entry')
