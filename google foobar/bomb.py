def solution(M, F):
    m, f = int(M), int(F)
    count = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m <= 0 and (m % 2 == 0 and f % 2 == 0):
            return "impossible"
        elif f == 1:
            return str(count + m - 1)
        else:
            count += int(m/f)
            m, f = f, m % f
    return str(count)


# count = 0


# def sol(x, y):
#     global count
#     if x > y:
#         x = x-y
#         count += 1
#         sol(x, y)
#     elif y > x:
#         y = y-x
#         count += 1
#         sol(x, y)
#     elif x == y and x != 1:
#         count = "impossible"
#
#
# def solution(x, y):
#     x = int(x)
#     y = int(y)
#     global count
#     sol(x, y)
#     return count


m = int(input('Enter m: '))
f = int(input('Enter f: '))

print(solution(m, f))


#print(solution(3, 2))
