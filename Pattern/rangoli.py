import string

alpha = string.ascii_lowercase

n = int(input("Num rows: "))
ls = []

for i in range(n):
    row = '-'.join(alpha[i:n])
    ls.append(row[::-1]+row[1:])

# print(l)
width = len(ls[0])

for i in range(n-1, 0, -1):
    print(ls[i].center(width, '-'))
for i in range(0, n):
    print(ls[i].center(width, '-'))
