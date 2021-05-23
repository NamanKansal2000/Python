n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i + 1):
        if i == 0 or k == 0 or k == 2*i or i == n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
