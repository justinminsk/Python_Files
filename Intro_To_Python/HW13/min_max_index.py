#list = [2, 3, 4, 5, 6, 7, 1, 4]
#index = 0
#for item in list:
#    smallest_index = 0
#    smallest_number = list[0]
#    if list[index] < smallest_number:
#        smallest_index = index
#        smallest_number = item


def min_index(num_list):
    smallest_index = 0
    index = 0
    smallest_number = num_list[0]
    for item in num_list:
        if item < smallest_number:
            smallest_index = index
            smallest_number = item
        index += 1
    result = (smallest_number, smallest_index)
    print(result)
    return result


def min_or_max_index(num_list, t_or_f):
    index = 0
    smallest_number = num_list[0]
    largest_number = num_list[0]
    if t_or_f:
        smallest_index = 0
        for item in num_list:
            if item < smallest_number:
                smallest_index = index
                smallest_number = item
            index += 1
        result = (smallest_number, smallest_index)
        print(result)
        return result
    else:
        largest_index = 0
        for item in num_list:
            if item > largest_number:
                largest_index = index
                largest_number = item
            index += 1
        result = (largest_number, largest_index)
        print(result)
        return result


if __name__ == '__main__':
    main_list = [2, 3, 4, 5, 6, 7, 1, 4]
    min_index(main_list)
    min_or_max_index(main_list, False)
