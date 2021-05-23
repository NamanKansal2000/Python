import random
from functools import cmp_to_key


def spiral(A):
    right, left = len(A) - 1, 0
    top, bottom = 0, len(A) - 1
    row, col = 0, 0
    direction = 0
    s = []
    for i in range(len(A)):
        if direction == 0:
            for col in range(left, right):
                s.append(A[row][col])
            top += 1
        if direction == 1:
            for row in range(top, bottom):
                s.append(A[row][col])
            right -= 1
        if direction == 2:
            for col in range(right, left, -1):
                s.append(A[row][col])
            bottom -= 1
        if direction == 3:
            for row in range(bottom, top, -1):
                s.append(A[row][col])
            left += 1
        direction = (direction + 1) % 4
    print(s)


def pascal_triangle(n):
    s = []
    for i in range(n):
        t = []
        for j in range(i+1):
            if i == j or j == 0:
                t.append(1)
            else:
                t.append(s[i-1][j]+s[i-1][j-1])
        s.append(t)
    print(s)


def largest_equal(A):
    start, stop = 0, 1
    curr = 0
    sum = 0
    flag = 0
    for i in range(len(A)):
        sum += 1 if A[i] == 1 else -1
        if sum == 0:
            flag = 1
            start = curr
            stop = i
            continue

    if flag == 0:
        return []
    print(A[start:stop])


def count_all_equal(A):
    sum = 0
    count = 0
    a = dict()
    for i in range(len(A)):
        sum += 1 if A[i] == 1 else -1

        if sum == 0:
            count += 1
        if sum in a.keys():
            count += a[sum]

        a[sum] = a.get(sum, 0) + 1
    print(count)


def flip(A):
    start = 0
    curr = 0
    ones = 0
    max_ones = 0
    ans = None
    for i in range(len(A)):
        ones += 1 if A[i] == '0' else -1
        if ones > max_ones:
            max_ones = ones
            start = curr
            # stop = i + 1
            ans = [start, i]
        if ones < 0:
            ones = 0
            curr = i + 1
    if ans is None:
        print('[]')
        return None
    # print('Index:- [{},{}]'.format(start, stop))
    print(list(map(lambda x: x + 1, ans)))


def diagonals(A):
    s = []
    for x in range(len(A)):
        t = []
        i, j = x, 0
        while i >= 0:
            t.append(A[i][j])
            i -= 1
            j += 1
        s.append(t)

    for x in range(1, len(A)):
        t = []
        i, j = len(A)-1, x
        while j < len(A):
            t.append(A[i][j])
            i -= 1
            j += 1
        s.append(t)
    print(s)


def largest_sum(A):
    sum = 0
    max_sum = None
    start = 0
    curr = 0
    for i in range(len(A)):
        sum += A[i]
        if i == 0:
            max_sum = sum
            start = curr
            stop = i + 1
        elif sum > max_sum:
            max_sum = sum
            start = curr
            stop = i + 1
        if sum < 0:
            sum = 0
            curr = i + 1
    print(A[start:stop])


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


def nobleInteger(A):
    counts = dict()
    for i in range(len(A)):
        counts[A[i]] = counts.get(A[i], 0) + 1
    for count in counts:
        if count == counts[count]:
            return 1
    return -1


def largestNumber(A):
    A = map(str, A)
    key = cmp_to_key(lambda a, b: 1 if a+b >= b+a else -1)
    array = sorted(A, key=key, reverse=True)
    num = ''.join(array[i] for i in range(len(array)))
    print(num)


def wave(A):
    A.sort()
    ls = []
    for i in range(len(A)-1):
        ls.append(i+1)
        ls.append(i)
    print(ls)


def hotel(A, D, k):
    events = [(t, 1) for t in A] + [(t, 0) for t in D]
    events.sort()
    guest = 0
    for event in events:
        if event[1] == 1:
            guest += 1
        else:
            guest -= 1
        if guest > k:
            return 0
    return 1


def maxDistance(A):
    ls = []
    for i in range(len(A)):
        ls.append([A[i], i])
    ls.sort()
    n = len(ls)
    print(ls)
    minI = ls[0][1]
    maxJ = ls[-1][1]
    print(minI, maxJ)
    while minI < n and maxJ < n:
        pass


A = [random.uniform(0, 3) for iter in range(100)]
print(A)
# maxDistance(A)
# B = [random.randint(1, 100) for iter in range(15)]
# k = random.randint(1, 10)
# print(A)
# print(B)
# print(k)
# print(hotel(A, B, k))
# wave(A)
# largestNumber(A)
# print(A)
# print(nobleInteger(A))

# largest_sum([-2, -3])
# flip('01000001')
# largest_equal([0, 0, 1, 1, 0])
# count_all_equal([0, 0, 1, 1, 0])
# max_non_negative_arr([1, 2, 5, -7, 2, 3])
