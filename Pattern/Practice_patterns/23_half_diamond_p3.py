n = int(input("Enter the height of pyramid: "))

count = 1
for i in range(n):
    for j in range(2*i+1):
        if j % 2 == 0:
            print(count, end='')
            count += 1
        else:
            print('*', end='')
    print()

count = count - n
for i in range(n):
    for j in range(2*n-2*i-1):
        if j % 2 == 0:
            print(count, end='')
            count += 1
        else:
            print('*', end='')
    count = count - 2*(n-i)+1
    print()
