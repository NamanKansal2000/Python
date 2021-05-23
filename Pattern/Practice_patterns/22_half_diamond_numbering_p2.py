n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(2*i+1):
        if j % 2 == 0:
            print(i+1, end='')
        else:
            print('*', end='')
    print()

for i in range(n):
    for j in range(2*n-2*i-1):
        if j % 2 == 0:
            print(n-i, end='')
        else:
            print('*', end='')
    print()
