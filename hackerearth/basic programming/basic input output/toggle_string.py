s = list(input())
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        s[i] = chr(ord('a')+ ord(s[i])-ord('A'))
    elif s[i]>='a' and s[i]<='z':
        s[i] = chr(-ord('a')+ ord(s[i])+ord('A'))
print(''.join(s))
