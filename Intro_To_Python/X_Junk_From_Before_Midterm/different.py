def different(num):
    """ (number) -> bool

    Return results as true if num is equal to abs(num).

    >>> different(-1)
    False
    >>> different(1)
    True
    """
    if num == abs(num):
        result = True
    else:
        result = False
    return result
