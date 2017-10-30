whalecounts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]


def find_two_smallest(L):
    # Examine each value in the list in order
    # Keep track of the indices of the two smallest values found so far
    # Update these values when a new smaller value is found
    # Return the two indices
    #...or
    # Set the first two values to smallest and smaller
    # Examine each value in the rest of the list
    # Update the minimum values when a new smaller value is found
    # Return the two indices
    # Set min1 and min2 to the indices of the smallest and next-smallest
    # Values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0
    # Examine each value in the list in order
    # Update min1 and/or min2 when a new smaller value is found **
    for i in range(2, len(L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
    # New second smallest?
        elif L[i] < L[min2]:
            min2 = i
    # Return the two indices
    return (min1, min2)


if __name__ == '__main__':
    print(find_two_smallest(whalecounts))