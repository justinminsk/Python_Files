whalecounts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]


def find_two_smallest(L):
    """ (list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """
    # Pseudocode:
    # Find the index of the minimum item in L
    # Remove that item from the list
    # Find the index of the new minimum item in the list
    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices of the smallest
    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)  # min2 index may have changed
    # Put the smallest item back in the list
    L.insert(min1, smallest)
    # If necessary, adjust the second index
    if min1 <= min2:
        min2 += 1
    # Return the two indices
    return (min1, min2)


if __name__ == '__main__':
    print(find_two_smallest(whalecounts))