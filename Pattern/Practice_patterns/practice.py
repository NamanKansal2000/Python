def half_pyramid(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print(j+1, end='')
        print()


def end():
    print()
    print('*******************')
    print()


def inverted_half_pyramid(n):
    for i in range(n):
        for j in reversed(range(n)):
            if j >= i:
                print(n-j, end='')
            else:
                print(' ', end='')
        print()


def hollow_half_pyramid(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                if i == 0 or i == n-1 or j == i or j == 0:
                    print(j+1, end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        print()


def full_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end=' ')
        for k in range(i+1):
            print(i+k+1, end=' ')
        for l in range(i):
            print(2*i - l, end=' ')
        print()


def hollow_full_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end=' ')
        for k in range(2*i+1):
            if i == 0 or i == n-1 or k == 0 or k == 2*i:
                if k % 2 == 0:
                    print(k//2 + 1, end=' ')
                else:
                    print(' ', end=' ')
            else:
                print(' ', end=' ')
        print()


def hollow_inverted_half_pyramid(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print(j+1, end=' ')

        print()


n = int(input("Enter the height of pyramid: "))
half_pyramid(n)
end()
inverted_half_pyramid(n)
end()
hollow_half_pyramid(n)
end()
full_pyramid(n)
end()
hollow_full_pyramid(n)
end()
hollow_inverted_half_pyramid(n)
