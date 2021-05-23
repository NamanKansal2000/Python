n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in reversed(range(n)):
        if j < i:
            print(' ', end='')
        else:
            print(n-j, end=' ')
    print()
