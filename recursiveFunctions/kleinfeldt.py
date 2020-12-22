def kleinfeldt(n):
    if n == 1:
        return 1
    else:
        return (1/(float(n*n)) + kleinfeldt(n-1))
