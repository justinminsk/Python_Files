def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(alist))
