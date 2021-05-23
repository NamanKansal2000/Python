def diagonal(A):
    s = []
    for x in range(len(A)):
        t = []
        i, j = x, 0
        while i >= 0:
            t.append(A[i][j])
            i -= 1
            j += 1
        s.append(t)
    # print(s)
    for x in range(1, len(A)):
        t = []
        i, j = len(A)-1, x
        while j < len(A):
            t.append(A[i][j])
            i -= 1
            j += 1
        s.append(t)
    print(s)


n = 5
c = 1
A = [[0 for i in range(n)]for j in range(n)]
for i in range(len(A)):
    for j in range(len(A)):
        A[i][j] = c
        c += 1
print(A)
diagonal(A)
