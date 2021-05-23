def repeatedNumber(A):
    n = len(A)
    temp = [0] * n
    for i in A:
        if temp[i-1]:
            return 1
        else:
            temp[i-1] = 1
