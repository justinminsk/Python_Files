import doctest

def average(values):
    """(list of numbers) -> number

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """
    count = 0
    total = 0
    for value in values:
        if value is not None:
            total += value
            count += 1
    return total / count


if __name__ == '__main__':
    doctest.testmod()
    print(average([-5, -2, 0, 1, 3, 4]))
