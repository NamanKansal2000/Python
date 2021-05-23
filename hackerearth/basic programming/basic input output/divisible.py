n = int(input())
s = input().split()
f = ''.join(list(map(lambda x:x[0], s[: (n//2)]))) + ''.join(list(map(lambda x:x[-1], s[(n//2) :])))
if int(f)%11 == 0:
    print('OUI')
else:
    print('NON')
