def pattern(n):
    ls = []

    for i in range(0, n):
        ls.append('*'*i)
    width = len(ls[n-1])
    for i in range(0, n):
        print((ls[i].rjust(width, ' ')))


n = int(input())
pattern(n)
