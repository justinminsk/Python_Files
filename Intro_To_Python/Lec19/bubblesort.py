def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # n times ; here: = range(8,0,-1)
        for i in range(passnum): # n times
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


if __name__ == '__main__':
    alist= [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)


def shortBubbleSort(alist):
    exchanges = True
    passnum= len(alist)-1
    while passnum> 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum= passnum-1


if __name__ == '__main__':
    alist=[20,30,40,90,50,60,70,80,100,110]
    shortBubbleSort(alist)
    print(alist)
