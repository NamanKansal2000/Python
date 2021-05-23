n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')

    for k in range(i + 1):
        print(k+1, end=' ')

    for l in range(i):
        print(i-l, end=' ')
    print()
