n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for k in range(2*i + 1):
        if i == 0 or k == 0 or k == 2*i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for k in range(2*n - 2*i - 1):
        if k == 0 or k == 2*n - 2*i - 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
