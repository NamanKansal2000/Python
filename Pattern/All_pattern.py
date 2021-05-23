import string


def upper_triangle(n):
    for i in range(1, n+1):
        print('*'*i)
    print('\n')


def lower_triangle(n):
    for i in range(n, 0, -1):
        print('*'*i)
    print('\n')


def upper_triangle_180(n):
    for i in range(0, n):
        print(' '*(n-i-1), '*'*(i+1))
    print('\n')


def lower_triangle_180(n):
    for i in range(n, 0, -1):
        print(' '*(n-i), '*'*i)
    print('\n')


def triangle_lst(n):
    ls = []
    sp = []
    for i in range(0, n):
        row = '*'*(2*i+1)
        ls.append(row)
    for i in range(n, 0, -1):
        space = ' '*(i-1)
        sp.append(space)
    # print(sp)
    for i in range(0, n):
        print(sp[i], ls[i])


def triangle(n):
    ls = []
    for i in range(n):
        s = '*'*(2*i+1)
        ls.append(s.center(2*n-1, ' '))
        # ls = ls[i].rjust(n-i, ' ')
        print(ls[i])
    # ls[i].rjust(' '*(n-i))
    # print(ls[i])


def bottom_triangle(n):
    ls = []
    for i in range(n):
        s = '*'*(2*(n-i)-1)
        s = s.center(2*n-1, ' ')
        ls.append(s)
        print(ls[i])


def rangoli(n):
    alpha = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))


# n = int(input('Enter no of rows: '))
n = 5
print()
upper_triangle(n)
print()
upper_triangle_180(n)
print()
lower_triangle(n)
pri

nt()
lower_triangle_180(n)
print()
triangle(n)
print()
bottom_triangle(n)








print()
rangoli(n)
print()
triangle_lst(n)
print()
