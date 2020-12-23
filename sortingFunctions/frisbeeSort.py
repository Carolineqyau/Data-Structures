def frisbeeSort(alist):
    l = len(alist)
    while l > 0:
        big = max(alist[0:l])
        index = alist.index(big)
        flip = alist[0:index+1]
        alist = flip[::-1]+alist[index+1:]
        l-=1
        flip = alist[0:l+1]
        alist = flip[::-1]+alist[l+1:]
    return alist
