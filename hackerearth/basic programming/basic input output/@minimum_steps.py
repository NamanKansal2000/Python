def rec(k,m,n,a):
    # if k > m then only way to reach to m is by following
    # steps 2 and 3 that is decreasing k
    if k>=m:
        return (k-m)//a+(k-m)%a
    # now if m is divisible by n then 1 step will be used to reduce m to m%n

    if m%n == 0:
        return 1+rec(k,m//n, n, a)
    # if m is not divisible the it is converted to above equation
    # using below mentioned steps
    else:
        x = (m//n + 1)*n
        return ((x-m)//a + (x-m)%a + rec(k,x,n,a))

t = int(input())
for i in range(t):
    k, m, n, a = map(int, input().split())
    print(rec(k,m,n,a))
