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
    # linear_search_3.py
    # add sentinel
    vlist.append(srchval)
    index = 0  # index of list item examined
    while vlist[index] != srchval:
        index += 1
    # remove sentinel
    vlist.pop()  # we have to remove it, the last one. we can use pop()
    if index == len(vlist):
        return -1
    else:
        return index


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)