def solve(A):
    A.sort()
    n = len(A)
    for i in range(n-1):
        if A[i] == A[i+1]:
            continue
        if A[i] == n - (i+1):
            return 1
    if A[n-1] == 0:
        return 1
    return -1


A = [-4, 7, 5, 3, 5]
print(A[2:len(A)-1])
print(solve([-4, 7, 5, 3, 5])
