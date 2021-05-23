t = int(input())
for _ in range(t):
    a = input()
    b = input()
    la = len(a)
    lb = len(b)
    d1 = {}
    d2 = {}
    # Logic is:
    # total length of both str - common char in both
    for i in range(la):
        if a[i] in d1.keys():
            d1[a[i]] += 1
        else:
            d1[a[i]] = 1
    # print('d1: ', d1)
    for i in range(lb):
        if b[i] in d2.keys():
            d2[b[i]] += 1
        else:
            d2[b[i]] = 1
    # print('d2: ', d2)
    s = 0
    for i in d1.keys():
        if i in d2.keys():
            s += min(d1[i] , d2[i])*2
    print(la+lb-s)
