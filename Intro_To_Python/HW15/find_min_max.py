def find_min_max(values):
    """(list of numbers) -> NoneType

    Print the minimum and maximum value from values.
    """
    min = values[0]  # start at the first number
    max = values[0]  # start at the first number
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value
    print('The minimum value is {0}'.format(min))
    print('The maximum value is {0}'.format(max))


if __name__ == '__main__':
    find_min_max([0, 1, 3, 4, 0, 2, -1])

    # None type screws up the list and produces an error
    # change line 6 and 7 to the first item on the list. This still does not help with mixed lists (string and num).
