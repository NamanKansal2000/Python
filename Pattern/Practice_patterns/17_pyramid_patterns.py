n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(2*n-i-2):
        print('*', end=' ')
    for k in range(2*i+1):
        if k % 2 == 0:
            print(i+1, end=' ')
        else:
            print('*', end=' ')
    for l in range(2*n-i-2):
        print('*', end=' ')
    print()
    print()
