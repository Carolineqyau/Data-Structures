def findLargest(list):
    if len(list) == 1:
        return list[0]
    else:
        if list[0] <= list[1]:
            return findLargest(list[1:])
        else:
            return findLargest([list[0]]+list[2:])
