n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(n-i-1):
        print('*', end=' ')
    print()
