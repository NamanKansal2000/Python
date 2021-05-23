n = 5
for i in range(n-1):
    for j in range(2*i+1):
        print('*', end='')
    for j in range(2*n-4*i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
