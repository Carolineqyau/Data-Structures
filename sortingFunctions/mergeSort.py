def mergeSort(alist):
    lefthalf = []
    righthalf = []
    if len(alist)>1:
        mid = len(alist)//2
        for m in range(mid):
            lefthalf.append(m)
        for n in range(mid,len(alist)):
            righthalf.append(n)
        i=0
        j=0
        k=0
        mlist = []
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                mlist.append(lefthalf[i])
                i+=1
            else:
                mlist.append(righthalf[j])
                j+=1
            k=k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            j=j+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1
        for a in lefthalf:
            mlist.append(a)
        for b in righthalf:
            mlist.append(b)
        return mlist
    else:
        return mlist
