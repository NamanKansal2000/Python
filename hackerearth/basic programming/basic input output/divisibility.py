n = int(input())
ls = list(map(lambda x:x[-1], input().split()))
s = int(''.join(ls))
if s%10 == 0:
    print('Yes')
else:
    print('No')
