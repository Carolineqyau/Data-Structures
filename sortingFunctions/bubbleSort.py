def bubbleSort(alist):
    for n in range(len(alist)-1,0,-1):
        for i in range(n):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
