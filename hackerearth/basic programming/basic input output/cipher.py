s = 'AaZz190./Usa'
k = 27
s = list(s)

for i in range(len(s)):
    if s[i]>= '0' and s[i]<= '9':
        val = (ord(s[i])-ord('0')+k)%10
        s[i] = chr(val+ord('0'))
    elif s[i]>='A' and s[i] <= 'Z':
        val = (ord(s[i])-ord('A') + k)%26
        s[i] = chr(val+ord('A'))

    elif s[i]>='a' and s[i]<='z':
        val = (ord(s[i])-ord('a') + k)%26
        s[i] = chr(val+ord('a'))
    else:
        continue

print(''.join(s))
