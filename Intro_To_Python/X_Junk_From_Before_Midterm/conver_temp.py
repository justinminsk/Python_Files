def convert_temperatures(t, source, target):
    """(number, String, String) -> float

        Take a temp. in one format and change it to a different format,
        allows Kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, Reaumur,
        and Romer.


        >>>convert_temperatures(25, 'Rankine', 'Romer')
        25 Rankine is now -128.61208333333335 Romer.
        >>>convert_temperatures(25, 'Celsius', 'Romer')
        25 Celsius is now 20.625 Romer.
        >>>convert_temperatures(20.625, 'Romer', 'Celsius')
        20.625 Romer is now 25.0 Celsius.
        """
    n = True
    told = t
    if source == 'Kelvin':
        t = t - 273.15
    elif source == 'Fahrenheit':
        t = (t - 32) * (5 / 9)
    elif source == 'Rankine':
        t = (t - 491.67) * 5 / 9
    elif source == 'Delisle':
        t = 100 - t *2/3 
    elif source == 'Newton':
            t = t * 100 / 33
    elif source == 'Reaumur':
        t = t * 5 / 4
    elif source == 'Romer':
        t = (t - 7.5) * 40 / 21
    elif source == 'Celsius':
        t = t
    else:
        print('Invaild source')
        n = False
    if target == 'Kelvin':
        t = t + 273.15
    elif target == 'Fahrenheit':
        t = t * 9 / 5 + 32
    elif target == 'Rankine':
        t = (t + 273.15) * 9 / 5
    elif target == 'Delisle':
        t = (100 - t) * 3 / 2
    elif target == 'Newton':
        t = t * 33 / 100
    elif target == 'Reaumur':
        t = t * 4 / 5
    elif target == 'Romer':
        t = t * 21 / 40 + 7.5
    elif target == 'Celsius':
        t = t
    else:
        print('Invaild target')
        n = False
    if n == True:
        print(told, source, "is now", t, target + ".")
    else:
        print('Invaild entries use captial letters for the begining of the sources')


