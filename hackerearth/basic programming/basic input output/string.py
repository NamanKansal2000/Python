t = int(input())
for i in range(t):
    lv = ['a', 'e', 'i', 'o', 'u']
    uv = ['A', 'E', 'I', 'O', 'U']
    s = input()
    l = [0]*5
    u = [0]*5
    flag = 0
    for i in s:
        if i in lv:
            l[lv.index(i)] = 1
        if i in uv:
            u[uv.index(i)] = 1
        if sum(l) == 5 or sum(u)==5:
            print('lovely string')
            flag = 1
            break
    if flag == 0:
        print('ugly string')
