def anti_diagonal(A):
    s = []
    for x in range(len(A)):
        i, j = x, 0
        t = []
        while i >= 0:
            t.append(A[i][j])
            i -= 1
            j += 1
        t.reverse()
        s.append(t)

    for x in range(1, len(A)):
        i, j = len(A)-1, x
        t = []
        while j < len(A):
            t.append(A[i][j])
            i -= 1
            j += 1
        t.reverse()
        s.append(t)
    print(s)
    return None


c = 1
n = 5
A = [[0 for i in range(n)]for j in range(n)]
for i in range(len(A)):
    for j in range(len(A)):
        A[i][j] = c
        c += 1
print(A)
anti_diagonal(A)
