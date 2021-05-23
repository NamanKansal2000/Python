n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n):
        if j >= i:
            if i == 0 or j == n-1 or j == i:
                print(j+1, end=' ')
            else:
                print(' ', end=' ')
    print()
