n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(i+1):
        if j == 0:
            print('*', end=' ')
        else:
            print(j, end=' ')
    for l in range(i):
        if l == i-1:
            print('*', end=' ')
        else:
            print(i-l-1,  end=' ')
    print()

for i in range(n-1):
    for j in range(n-i-1):
        if j == 0:
            print('*', end=' ')
        else:
            print(j, end=' ')
    for l in range(n-i-2):
        if l == n-i-3:
            print('*', end=' ')
        else:
            print(n-i-l-3, end=' ')
    print()
