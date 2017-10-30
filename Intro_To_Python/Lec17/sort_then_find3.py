whalecounts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]


def find_two_smallest(L):
    """ (see before) """
    # Get a sorted copy of the list so that the two smallest items are at the
    # front
    temp_list= sorted(L)
    smallest = temp_list[0]
    next_smallest= temp_list[1]
    # Find their indices in the original list L
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    # Return the indices of the two
    return (min1, min2)


if __name__ == '__main__':
    print(find_two_smallest(whalecounts))