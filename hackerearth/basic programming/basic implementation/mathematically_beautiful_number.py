t = int(input())
while t > 0:
    t -= 1
    x, k = map(int, input().split())
    good = True
    while x > 0:
        good &= x % k < 2
        x //= k
    print("YES" if good else "NO")
