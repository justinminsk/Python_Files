def list_by_mag(num_list):
    for nums in range(len(num_list) - 1, 0, -1):
        for i in range(nums):
            if abs(num_list[i]) > abs(num_list[i + 1]):
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp
            if abs(num_list[i]) == abs(num_list[i + 1]):
                if num_list[i] > num_list[i + 1]:
                    temp = num_list[i]
                    num_list[i] = num_list[i + 1]
                    num_list[i + 1] = temp
                else:
                    temp = num_list[i + 1]
                    num_list[i + 1] = num_list[i]
                    num_list[i] = temp
            if abs(num_list[i]) == abs(num_list[i - 1]):
                if num_list[i] > num_list[i - 1]:
                    temp = num_list[i]
                    num_list[i] = num_list[i - 1]
                    num_list[i - 1] = temp


if __name__ == '__main__':
    num_list = [-2, -1, 2, 3, -5, 4, 2, -2, -4]
    list_by_mag(num_list)
    print(num_list)