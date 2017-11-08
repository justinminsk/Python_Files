def dutch_flag(color_list):
    end_list = []
    for color in color_list:
        if color == 'red':
            end_list.insert(0, 'red')
        elif color == 'blue':
            index_count = 0
            for new_color in end_list:
                index_count += 1
            end_list.insert(index_count, 'blue')
        elif color == 'green':
            index_count = 0
            for new_color in end_list:
                if new_color == 'red':
                    index_count += 1
                else:
                    end_list.insert(index_count, 'green')
                    break
    return end_list


if __name__ == '__main__':
    flag_list = ['green', 'red', 'blue', 'green', 'red', 'green', 'blue', 'green', 'blue', 'green', 'blue', 'red',
                 'blue', 'red',
                 'green', 'green', 'green', 'green']
    print(dutch_flag(flag_list))