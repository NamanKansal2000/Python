n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n):
        if j <= i:
            if i == 0 or j == 0 or i == n-1 or i == j:
                print(j+1, end=' ')
            else:
                print(' ', end=' ')
    print()
