n = int(input())
s = input().split()
m = 1
for i in s:
    m *= int(i)
    m %= (10**9 + 7)
print(m)
