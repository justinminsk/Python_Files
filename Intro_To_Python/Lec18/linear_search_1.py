def linear_search(vlist, srchval): # somewhat different from book
    """ (list, object) -> int
    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    # linear_search_1.py
    # let's try a while statement first
    # we need the index, and then a way to stop
    index = 0 # index of list item examined
    # vlist= values list; searchval
    while index != len(vlist) and vlist[index] != srchval:
        index += 1
    if index == len(vlist):
        return -1
    else:
        return index


if __name__ == '__main__':
    import doctest
    doctest.testmod()