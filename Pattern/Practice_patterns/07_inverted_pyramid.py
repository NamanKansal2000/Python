n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(n-i) - 1):
        print('*', end='')
    print()
