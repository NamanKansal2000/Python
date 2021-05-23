def wave(A):
    A.sort()
    print(A)
    ls = []
    for i in range(0, len(A)-1, 2):
        ls.append(A[i+1])
        ls.append(A[i])
    if len(A) % 2 is not 0:
        ls.append(A[len(A)-1])
    return ls


print(wave([5, 1, 3, 2, 4]))
