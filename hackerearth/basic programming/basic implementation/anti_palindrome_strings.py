t=int(input())
for _ in range(t):
    s=input()
    s = ''.join(sorted(list(s)))
    if s == s[::-1]:
        print('-1')
    else:
        print(s)
