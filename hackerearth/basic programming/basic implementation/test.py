def sum_digits(n):
    s = 0
    for i in str(n):
        s+=int(i)
    return s


s = '70202 49919'
n, k = map(int, s.split())
d = {}
for i in range(k):
    if n not in d.keys():
        d[n] = sum_digits(n)**3
        n = sum_digits(n)**3
    else:
        n = d[n]
print(d)
print(n)
