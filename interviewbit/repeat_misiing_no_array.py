# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which
# is missing.
#
# Return A and B.
#
# Note: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


def repeated(A):
    A = list(A)
    a = sum(A)-sum(list(set(A))  # repeated no
    n=len(A)
    b=a - sum(A) + n*(n+1)/2  # missing no
    return a, b
