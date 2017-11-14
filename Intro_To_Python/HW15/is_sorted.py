def is_sorted(lst):
    lst_temp = lst
    lst_temp = sorted(lst_temp)
    if lst == lst_temp:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_sorted([]))