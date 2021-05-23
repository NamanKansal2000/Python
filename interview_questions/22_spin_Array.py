def spiralOrder(a):
    row = len(a)
    col = len(a[0])
    k = 0
    l = 0
    B= []
    while k < row and l < col:
        for i in range(l, col):
            B.append(a[k][i])
        k+=1
        for i in range(k, row):
            B.append(a[i][col-1])
        col-=1
        for i in range(col-1, l-1,-1):
            B.append(a[row-1][i])
        row-=1
        for i in range(row-1, k-1, -1):
            B.append(a[i][l])
        l+=1
    return B

A = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
# A = [[1]]
print(spiralOrder(A))
