n = int(input("Enter the height of pyramid: "))

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for k in range(2*i+1):
        if i == 0 or i == n-1 or k == 0 or k == 2*i:
            if k % 2 == 0:
                print(k//2 + 1, end='')
            else:
                print(' ', end='')
        else:
            print(' ', end='')
    print()
