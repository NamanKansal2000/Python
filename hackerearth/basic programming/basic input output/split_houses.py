n = int(input())
s = input()
original = s
s = list(s)
flag = False
for i in range(n):
    if s[i] == '.':
        s[i] = 'B'
s = ''.join(s)
for i in range(n-1):
    if s[i] == 'H' and s[i+1] == 'H':
        flag = True
        break
if (flag or (original == s)) and n!=1:
    print('NO')
else:
    print('YES')
    print(s)
