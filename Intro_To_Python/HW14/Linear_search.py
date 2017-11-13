def lin_search1(list, value):
    i = len(list) - 1  # get i to the last index
    while i != 0 and list[i] != value:  # go through the list
        i = i - 1  # look at next index
    if i == 0:  # if it goes through the list
        return -1
    else:
        return i


def lin_search2(list, value):
    for i in range(len(list) - 1, -1, -1):  # go from last number to first
        if list[i] == value:  # if the list has the value
            return i
    return -1


def lin_search3(list, value):
    list.insert(0, value)  # insert the sent value
    i = len(list) - 1  # make i at the end of the list
    while list[i] != value:  # go through the list
        i = i - 1
    list.pop(0)
    if i == 0:
        return -1
    return i - 1


if __name__ == '__main__':
    print(lin_search1([0, 1 , 2, 3, 4], 4))
    print(lin_search2([0, 1 , 2, 3, 4], 4))
    print(lin_search3([0, 1 , 2, 3, 4], 4))

# Nlog_2 N + S * Nlog_2 N < S * N
# 2 * log_2 N < S
