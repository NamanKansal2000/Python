def pascalTriangle(n):
    a = []
    for i in range(n):
        t = []
        for j in range(i+1):
            if j == 0 or i == j:
                t.append(1)
            else:
                t.append(a[i-1][j]+a[i-1][j-1])
        a.append(t)

    return a


A = (pascalTriangle(80))
# to access kth row
