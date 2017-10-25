def count_dup(dict):
    count = 0  # create a count
    for entry in dict:
        if dict[entry] > 1:  # if the the list for each key of the dict is greater than 1
            count += 1  # increase count by one
    print(count)  # print count
    return count  # return count


if __name__ == '__main__':
    dict = {'red': 1, 'green': 1, 'blue': 2}
    count_dup(dict)