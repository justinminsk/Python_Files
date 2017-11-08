def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # n times ; here: = range(8,0,-1)
        for i in range(passnum): # n times
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


if __name__ == '__main__':
    alist= [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)


def shortBubbleSort(alist):
    exchanges = True
    passnum= len(alist)-1
    while passnum> 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum= passnum-1


if __name__ == '__main__':
    alist=[20,30,40,90,50,60,70,80,100,110]
    shortBubbleSort(alist)
    print(alist)


def selection_sort(L):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> selection_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> selection_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> selection_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> selection_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """
    i= 0
    while i != len(L):
        # Find the index of the smallest item in L[i:]
        # a fast way: L.index(min(L))
        # without using min(0 function:
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1


def find_min(L, b):
    smallest = b  # The index of the smallest so far.
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # We found a smaller item at L[i].
            smallest = i
        i = i + 1
    return smallest


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)


def insert(L,b):
    """ (list, int) -> NoneType
    Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """
    # Find where to insert L[b] by searching backwards from L[b]
    # for a smaller item.
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1
    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b]
    L.insert(i, value)


def insertion_sort(L):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> insertion_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> insertion_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> insertion_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> insertion_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> insertion_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> insertion_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """
    i = 0
    while i != len(L):
        insert(L, i)
        i = i + 1


# doctest with verbose = True
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1) # recursive
        quickSortHelper(alist,splitpoint+1,last) # recursive


def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20] # list(range(900,0,-1))
    quickSort(alist)
    print(alist)
    alist = list(range(900,0,-1))
    quickSort(alist)
    print(alist)
