from functools import cmp_to_key


class Solution:
    def minSteps(self, A, B):
        count = 0
        for i in range(len(A)-1):
            count += max(abs(A[i]-A[i+1]), abs(B[i]-B[i+1]))
        return count

    def addOne(self, A):
        A = map(str, A)
        num = int(''.join(A)) + 1
        num = str(num)
        ls = []
        for i in range(len(num)):
            ls.append(num[i])
        return ls

    def maxArray(self, A):
        start, stop = 0, 1
        max_sum = None
        sum = 0
        curr = 0
        for i in range(len(A)):
            sum += A[i]
            if i == 0:
                max_sum = sum
                start = curr
                stop = i+1
            elif sum > max_sum:
                max_sum = sum
                start = curr
                stop = i+1
            if sum < 0:
                sum = 0
                curr = i + 1
        max_sum_arr = A[start:stop]
        return max_sum, max_sum_arr

    def maxAbsoluteDifference(self, A):
        p = []
        n = []
        for i in range(len(A)):
            p.append(A[i] + i)
            n.append(A[i] - i)
        m1, m2 = min(p), max(p)
        m3, m4 = max(n), min(n)
        return max(abs(m1-m2), abs(m3-m4))

    def repeatedMissingNumber(self, A):
        n = len(A)
        a = sum(A) - sum(set(A))
        b = int((n*(n+1)/2) + a - sum(A))
        return [a, b]

    def flip(self, A):
        start, stop = 0, 1
        ones = 0
        max_ones = 0
        curr = 0
        ans = None
        for i in range(len(A)):
            ones += 1 if A[i] == '0' else -1
            if ones > max_ones:
                max_ones = ones
                start = curr
                stop = i
                ans = [start, stop]
            if ones < 0:
                ones = 0
                curr = i + 1
        if ans is None:
            return []
        ans = map(lambda x: x+1, ans)
        return list(ans)

    def maxNonNegativeArr(self, A):
        n = []
        ls = []
        for i in range(len(A)):
            if A[i] >= 0:
                n.append(A[i])
            else:
                if n != []:
                    ls.append(n)
                n = []
        val = []
        for i in range(len(ls)):
            val.append(sum(ls[i]))
        return ls[val.index(max(val))]

    def spiral_matrix_II(self, A):
        ls = [[0 for i in range(A)]for j in range(A)]
        c = 1
        for i in range(A):
            for j in range(A):
                ls[i][j] = c
                c += 1
        print(ls)
        direction, row, col = 0, 0, 0
        left, right = 0, A - 1
        top, bottom = 0, A - 1
        spiral = []
        while(left <= right and top <= bottom):
            if direction == 0:
                for col in range(left, right+1):
                    spiral.append(ls[row][col])
                top += 1
            if direction == 1:
                for row in range(top, bottom+1):
                    spiral.append(ls[row][col])
                right -= 1
            if direction == 2:
                for col in reversed(range(left, right+1)):
                    spiral.append(ls[row][col])
                bottom -= 1
            if direction == 3:
                for i in reversed(range(top, bottom+1)):
                    spiral.append(ls[row][col])
                left += 1
            direction = (direction + 1) % 4
        return spiral

    def pascal_triangle(self, n):
        ls = []
        for i in range(n):
            n = []
            for j in range(i+1):
                if i == j or j == 0:
                    n.append(1)
                else:
                    n.append(ls[i-1][j]+ls[i-1][j-1])
            ls.append(n)
        return ls

    def antiDiagonal(self, A):
        ls = []
        for x in range(len(A)):
            n = []
            i, j = x, 0
            while i >= 0:
                n.append(A[i][j])
                i -= 1
                j += 1
            ls.append(list(reversed(n)))
        for x in range(1, len(A)):
            n = []
            i, j = len(A)-1, x
            while j < len(A):
                n.append(A[i][j])
                i -= 1
                j += 1
            ls.append(list(reversed(n)))
        return ls

    def nobleInterger(self, A):
        A.sort()
        if A[len(A)-1] == 0:
            return 1
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                continue
            if A[i] == len(A) - i - 1:
                return 1
        return -1

    def largestNumber(self, A):
        A = map(str, A)
        key = cmp_to_key(lambda a, b: 1 if b+a >= a+b else -1)
        A = sorted(A, key=key)
        return ''.join(i for i in A)

    def wave(self, A):
        A.sort()
        n = len(A)
        ls = []
        for i in range(n-1):
            ls.append(A[i+1])
            ls.append(A[i])
        return ls

    def hotel(self, A, D, K):
        events = [(t, 1) for t in A] + [(t, 0) for t in D]
        guests = 0
        events.sort()
        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1
            if guests > K:
                return 1
        return 0

    def maximumGap(self, A):
        arr = list(A)
        counts = dict()
        for i in range(len(arr)):
            if arr[i] in counts:
                counts[arr[i]].append(i)
            else:
                counts[arr[i]] = [i]
        arr.sort()
        diff = 0
        temp = len(arr)
        for i in range(len(arr)):
            if temp > counts[arr[i]][0]:
                temp = counts[arr[i]][0]
            diff = max(diff, counts[arr[i]][-1] - temp)
        return diff

    def subUnsort(self, A):
        B = sorted(A)
        for i in range(len(A)):
            A[i] = A[i] - B[i]
        start, end = -1, -1
        for i in range(len(A) - 1):
            if A[0] != 0:
                start = 0
                break
            if A[i] == 0 and A[i+1] != 0:
                start = i + 1
                break
        for i in reversed(range(0, len(A) - 1)):
            if A[len(A) - 1] != 0:
                end = len(A) - 1
                break
            if A[i] == 0 and A[i-1] != 0:
                end = i - 1
                break
        if start == -1 and end == -1:
            return [-1]
        return [start, end]

    def repeatedNumber(self, A):
        arr = [0]*len(A)
        for i in A:
            if arr[i-1]:
                return i
            else:
                arr[i - 1] = 1
        return -1

    def maxConsectiveGap(self, A):
        A = list(A)
        if len(A) < 2:
            return 0
        A.sort()
        diff = 0
        for i in range(len(A) - 1):
            diff = max(diff, A[i + 1] - A[i])
        return diff

    def maxSpecialProduct(self, A):
        pass

    def rotate_90_clockwise(self, A, k):
        # transpose of A
        k = (k // 90) % 4
        for i in range(k):
            for i in range(len(A)):
                for j in range(i, len(A)):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
            n = len(A)
            for i in range(n):
                for j in range(n//2):
                    A[i][j], A[i][n-1-j] = A[i][n-1-j], A[i][j]
        return A

    def rotate_r(self, A, r):
        for rounds in range(r):
            top, bottom = 0, len(A) - 1
            left, right = 0, len(A) - 1
            while left <= right and top <= bottom:
                prev = A[top+1][left]
                for i in range(left, right + 1):
                    curr = A[top][i]
                    A[top][i] = prev
                    prev = curr
                top += 1
                for i in range(top, bottom + 1):
                    curr = A[i][right]
                    A[i][right] = prev
                    prev = curr
                right -= 1
                for i in reversed(range(left, right+1)):
                    curr = A[bottom][i]
                    A[bottom][i] = prev
                    prev = curr
                bottom -= 1
                for i in reversed(range(top, bottom + 1)):
                    curr = A[i][left]
                    A[i][left] = prev
                    prev = curr
                left += 1
        return A


obj = Solution()
A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(obj.rotate_r(A, 2))
