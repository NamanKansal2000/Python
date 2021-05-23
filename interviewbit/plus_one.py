# Given a non-negative number represented as an array of digits,
#
# add 1 to the number ( increment the number represented by the digits ).
#
# The digits are stored such that the most significant digit is at the head of
# the list.
#
# Example:
#
# If the vector has [1, 2, 3]
#
# the returned vector should be [1, 2, 4]
#
# as 123 + 1 = 124.


def plusone(A):
    for i in range(len(A)):
        A[i] = str(A[i])
    s = ''.join(A)
    num = int(s)
    num += 1
    num = str(num)
    ls = []
    for i in range(len(num)):
        ls.append(num[i])

    return ls
