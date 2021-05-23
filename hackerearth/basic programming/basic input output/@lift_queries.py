t = int(input())
a = 0
b = 7
for _ in range(t):
    f = int(input())
    if abs(f-a) <= abs(f-b):
        print('A')
        a = f
    else:
        print('B')
        b = f
