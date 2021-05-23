n = 21
m = 3*n
w = 'WELCOME'
for i in range(n//2):
    for j in range((n//2-i)*3):
        print('-', end = '')
    for j in range(2*i+1):
        print('.|.', end='')
    for j in range((n//2-i)*3):
        print('-', end = '')

    print()
if n%2 == 0:
    print(((m-len(w))//2 + 2) * '-' + w + ((m-len(w))//2 + 2)* '-')
else:
    print((m-len(w))//2 * '-' + w + (m-len(w))//2 * '-')

for i in range(n//2):
    for j in range(3*(i+1)):
        print('-', end='')
    if n%2 == 0:
        for j in range(2* n//2 -2*i - 1):
            print('.|.', end='')
    else:
        for j in range(2* n//2 -2*i-2):
            print('.|.', end='')
    for j in range(3*(i+1)):
        print('-', end='')
    print()
