t = int(input())
for _ in range(t):
    c = list(map(int, input().split()))
    n = int(input())
    q = [0,0]
    for i in range(n):
        a, b = map(int, input().split())
        q[0] += a
        q[1] += b
    print(min(q[0]*c[0]+q[1]*c[1], q[0]*c[1]+q[1]*c[0]))
