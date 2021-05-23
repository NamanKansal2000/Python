d = {}
ls = []
while 1:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    d[a] = d.get(a,0)+1
    d[b] = d.get(b,0)+1
    ls.append([a,b])
a = []
for i in d.keys():
    if d[i]>1:
        a.append(i)
for i in ls:
    if i[0] in a:
        print('0 1')
    elif i[1] in a:
        print('1 0')
    else:
        print('-1 -1')
