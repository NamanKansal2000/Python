t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print((abs((b-a)-(c-b))+1)//2)
