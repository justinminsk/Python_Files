def dict_interest(dict1, dict2):
    end_result = {}  # create the dict we will enter into
    for (index, value) in dict1.items():  # look at both key and value in dict1
        if index in dict2 and value == dict2[index]:  # if key is in dict2 and value equals value in dict2
            end_result[index] = value  # add the key and value to the end result
    print(end_result)  # print end result
    return end_result  # return end result


if __name__ == '__main__':
    dict1 = {'hi': 1, 'bye': 2, "i": 3}
    dict2 = {'hi': 2, 'bye': 2, "j": 3}
    dict_interest(dict1, dict2)