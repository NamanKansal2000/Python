def max_non_negative_arr(A):
    t = []
    s = []
    for i in range(len(A)):
        if A[i] < 0:
            if t is not []:
                s.append(t)
            t = []
        else:
            t.append(A[i])

    val = []
    for i in range(len(s)):
        val.append(sum(s[i]))

    i = val.index(max(val))
    print(s[i])


max_non_negative_arr([1, 2, 5, -7, 2, 3, -1, 0, 3, 5])
