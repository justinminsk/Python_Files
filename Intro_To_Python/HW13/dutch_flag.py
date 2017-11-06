def dutch_flag(flag_list):
    end_list = []
    for item in flag_list:
        if item == 'red':
            end_list.insert(0, 'red')
        if item == 'green':
            index = 0
            for color in end_list:
                if color != 'red':
                    end_list.insert(index, 'green')
                    break
                index += 1
        if item == 'blue':
            index = 0
            for color in end_list:
                index += 1
            end_list.insert(index, 'blue')
    print(end_list)
    return end_list


if __name__ == '__main__':
    flag_list = ['green','red','blue','green','red','green','blue','green','blue','green','blue','red','blue','red',
                 'green','green','green','green']
    dutch_flag(flag_list)