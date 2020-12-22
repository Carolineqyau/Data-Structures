def ternarySearchRec(alist, item):
    if alist == []:
        return False
    else:
        mid1 = len(alist)//3
        mid2 = 2*len(alist)//3
        if alist[mid1] == item or alist[mid2] == item:
            return True
        elif item < alist[mid1]:
            return ternarySearchRec(alist[:mid1], item)
        elif item > alist[mid2]:
            return ternarySearchRec(alist[mid2+1:], item)
        else:
            return ternarySearchRec(alist[mid1+1:mid2], item)
