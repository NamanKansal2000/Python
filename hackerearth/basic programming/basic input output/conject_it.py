t = int(input())
for _ in range(t):
    n = int(input())
    flag = True
    while flag:
        # print(n)
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        if n <=1:
            flag = False
    if n == 1:
        print('YES')
    else:
        print('NO')
