def count_values(dict):
    count = 0  # create a count
    for entry in dict:
        if dict[entry] == 1:  # if the number value is equal to 1
            count += 1  # increase count by 1
    print(count)  # print count
    return count  # return count


if __name__ == '__main__':
    dict = {'red': 1, 'green': 1, 'blue': 2}
    count_values(dict)