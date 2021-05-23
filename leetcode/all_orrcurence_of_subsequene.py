a = 'HSSSSSSSSSSJJDILLL'
b = 'HSL'
m = len(a)
n = len(b)
ls = [[0 for _ in range(n+1)] for _ in range(m+1)]

for i in range(n+1):
    ls[0][i] = 0
for i in range(m+1):
    ls[i][0] = 1



for i in range(1,m+1):
    for j in range(1, n+1):
        if a[i-1] == b[j-1]:
            ls[i][j] = ls[i-1][j-1]+ls[i-1][j]

        else:
            ls[i][j] = ls[i-1][j]

for i in range(m+1):
    print(ls[i])
