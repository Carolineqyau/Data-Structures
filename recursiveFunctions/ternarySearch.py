def ternarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        mid1 = first + (last - first)//3
        mid2 = last - (last - first)//3
        if alist[mid1] == item or alist[mid2] == item:
            found = True
        else:
            if item < alist[mid1]:
                last = mid1 - 1
            elif item > alist[mid2]:
                first = mid2 + 1
            else:
                first = mid1 + 1
                last = mid2 - 1
    return found
