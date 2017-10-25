def find_dubs(list):
    count_list = {}  # create a dict count list
    final_list = []  # create a list named final list
    for entry in list:
        if entry in count_list:  # if entry is in count list
            count_list[entry].append(entry)  # add the entry to the list side of the dict
        else:
            count_list[entry] = [entry]  # make the key the entry and add the entry to the list
    for entry in count_list:
        if len(count_list[entry]) >= 2:  # if the list length is longer than or equal to 2
            final_list.append(entry)  # add the entry to the list
    print(final_list)  # print the final list
    return final_list  # return the final list


if __name__ == '__main__':
    intlist = [1, 2, 3, 3, 4, 4, 5, 6, 7, 3, 2, 3, 4, 3, 4, 5, 5]
    find_dubs(intlist)