n = int(input())
# n = 4
for k in range(n):
    for i in range(5):
        for j in range(5):
            if i == 4 or ((i == 1 or i == 3) and (j == 0 or j == 4)):
                print('*', end='')
            else:
                print(' ', end='')
        print()
for i in range(4):
    for j in range(5):
        if ((i == 1 or i == 3) and (j == 0 or j == 4)):
            print('*', end='')
        else:
            print(' ', end='')
    print()
