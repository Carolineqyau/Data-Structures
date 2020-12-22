def ladder(n):
    if n == 0 or n == 1:
        return 1
    else:
        return ladder(n-1) + ladder(n-2)
