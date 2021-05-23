from functools import cmp_to_key


def compare(a, b):
    a = str(a)
    b = str(b)
    return 1 if int(a+b) >= int(b+a) else -1


def largestNumber(A):
    A = list(map(str,A))
    A = sorted(A, key=lambda a,b:key(a+b, b+a), reverse=True)
    return(''.join(str(i) for i in A))


print(largestNumber([12, 43, 765, 890, 32, 12, 2, 3, 13, 9]))
