d = int(input())
t = 0
for _ in range(d):
    r, x = map(int, input().split())
    dis = 100*x
    cdis = 2* (22/7)* (r)
    if dis >= cdis:
        t+=1
print(t)
