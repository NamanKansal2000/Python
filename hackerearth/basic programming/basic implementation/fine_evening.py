import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    days = 0
    if k<=n:
        days = math.ceil(math.log(k,2))+1
    else:
        dn = math.ceil(math.log(n,2))+1
        m = k//n
        days = (m*dn)+math.ceil(math.log(k%n,2))+1
    print(days)
