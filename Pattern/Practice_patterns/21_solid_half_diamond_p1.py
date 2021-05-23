n = int(input("Enter the height of pyramid: "))

for i in range(n+1):
    for j in range(i+1):
        print(i+3, end=' ')
    print()

for i in range(n):
    for j in range(n-i):
        print(2*n-1-i, end=' ')
    print()
