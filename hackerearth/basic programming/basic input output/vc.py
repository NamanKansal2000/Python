t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    for i in range(n-1):
        if (s[i] not in ['a','e', 'i', 'o', 'u']) and (s[i+1] in ['a','e', 'i', 'o', 'u']):
            count+=1
    print(count)
