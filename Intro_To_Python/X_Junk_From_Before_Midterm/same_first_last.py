def same_first_last(L):
    """(list)->bool
    Precon: len(L) <= 2

    Return true if and only if first item of the list is the same as the last.

    >>>same_first_last([3, 4, 2, 8, 3])
    True
    >>>same_first_last(['apple', 'banana', 'pear'])

    >>>same_first_last([4.0, 4.5])

    """
    if L[0] == L[-1]:
        return True
    
