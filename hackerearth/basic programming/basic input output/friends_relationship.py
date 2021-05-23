t = int(input())
for val in range(t):
    n = int(input())
    for i in range(1, n+1):
        for j in range(i):
            print('*', end = '')
        for j in range(1, 2*(n-i)+1):
            print('#', end='')
        for j in range(i):
            print('*', end='')
        print()
