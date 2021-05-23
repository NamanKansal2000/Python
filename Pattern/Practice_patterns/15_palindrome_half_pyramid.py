n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    for k in range(i):
        print(i-k, end=' ')
    print()
