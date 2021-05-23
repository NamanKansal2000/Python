n, q = map(int, input().split())
s = input().split()
s[0] = int(s[0])
for i in range(1, n):
    s[i] = int(s[i-1])+int(s[i])
for _ in range(q):
    l, r = map(int, input().split())
    l-=1
    r-=1
    if l==0:
        print(s[r]//(r+1))
        continue
    print((s[r]-s[l-1])//(r-l+1))
