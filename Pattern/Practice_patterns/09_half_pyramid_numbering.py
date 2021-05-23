n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n):
        if j <= i:
            print(j+1, end=' ')
    print()
