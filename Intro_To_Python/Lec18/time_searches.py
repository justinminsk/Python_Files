import time
import linear_search_1
import linear_search_2
import linear_search_3


def time_it(search, L, v):
    """ (function, object, list) -> number
    Time how long it takes to run function search to find
    value v in list L.
    """
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 -t1) * 1000.0


def print_times(v, L):
    """ (object, list) -> NoneType
    Print the number of milliseconds it takes for linear_search(v, L)
    to run for list.index, the while loop linear search, the for loop
    linear search, and sentinel search.
    """
    # Get list.index'srunning time.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time= (t2 -t1) * 1000.0
    # Get the other three running times.
    while_time= time_it(linear_search_1.linear_search, L, v)
    for_time= time_it(linear_search_2.linear_search, L, v)
    sentinel_time= time_it(linear_search_3.linear_search, L, v)
    print("{0}\t{1:>6.1f}\t{2:>6.1f}\t{3:>6.1f}\t{4:>6.1f}".format(v, while_time, for_time, sentinel_time, index_time))
    # modified to make it easier to change values


if __name__ == '__main__':
    ListLength= 10000001 # default: 10,000,001
    L = list(range(ListLength)) # A list of variable length
    print ('Search times in a list of ' , "{:,}".format(ListLength) ) # title,listsize,commas
    print ('Index\t while\t for\t Sent\t.index') # tabbed column headings
    print_times(10, L) # How fast is it to search near the beginning?
    print_times(round(ListLength/2), L) # How fast is it to search near the middle?
    print_times(ListLength-50, L) # How fast is it to search near the end?