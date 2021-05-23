class Solution:
    def minSteps(self, A, B):
        counts = 0
        for i in range(len(A) - 1):
            counts += max(abs(A[i+1] - A[i]), abs(B[i+1] - B[i]))
        return counts

    def plusOne(self, A):
        A = map(str, A)
        num = int(''.join(i for i in A)) + 1
        num = str(num)
        ls = []
        for i in range(len(num)):
            ls.append(num[i])
        return map(int, ls)

    def maxSubArray(self, A):
        A = list(A)
        start, stop = 0, 1
        curr = 0
        sum = 0
        max_sum = None
        for i in range(len(A)):
            sum += A[i]
            if i == 0:
                max_sum = sum
                start = curr
                stop = i+1
            if sum > max_sum:
                max_sum = sum
                start = curr
                stop = i+1
            if sum < 0:
                sum = 0
                curr = i+1
        return max_sum

    def maxArr(self, A):
        p = []
        n = []
        for i in range(len(A)):
            p.append(A[i] + i)
            n.append(A[i] - i)
        m1, m2 = max(p), min(p)
        m3, m4 = max(n), min(n)
        return max(abs(m1 - m2), abs(m3 - m4))

    def repeatedNumber(self, A):
        A = list(A)
        B = set(A)
        a = sum(A) - sum(B)
        n = len(A)
        b = n*(n+1)/2 + a - sum(A)
        return a, int(b)

    def flip(self, A):
        start, stop = 0, 1
        curr = 0
        ones = 0
        max_ones = 0
        ans = None
        for i in range(len(A)):
            ones += 1 if A[i] == '0' else -1
            if ones > max_ones:
                max_ones = ones
                start = curr
                ans = [start, i]
            if ones < 0:
                ones = 0
                curr = i + 1
        if ans is None:
            return []
        return list(map(lambda x: x+1, ans))

    def maxset(self, A):
        if len(A) <= 1:
            return A
        ls = []
        n = []
        for i in range(len(A)):
            if A[i] >= 0:
                n.append(A[i])
            else:
                ls.append(n)
                n = []
        val = []
        for i in range(len(ls)):
            val.append(sum(ls[i]))
        return ls[val.index(max(val))]

    def generateMatrix(self, A):
        ls = []
        ls = [[0 for i in range(A)]for i in range(A)]
        c = 1
        for i in range(A):
            for j in range(A):
                ls[i][j] = c
                c += 1
        print(ls)
        left, right = 0, A - 1
        top, bottom = 0, A - 1
        row, col = 0, 0
        direction = 0
        s = []
        while left <= right and top <= bottom:
            if direction == 0:
                for col in range(left, right + 1):
                    s.append(ls[top][col])
                top += 1
            if direction == 1:
                for row in range(top, bottom+1):
                    s.append(ls[row][right])
                right -= 1
            if direction == 2:
                for col in reversed(range(left, right + 1)):
                    s.append(ls[bottom][col])
                bottom -= 1
            if direction == 3:
                for row in reversed(range(top, bottom + 1)):
                    s.append(ls[row][left])
                left += 1
            direction = (direction + 1) % 4
        return s


obj = Solution()

print(obj.generateMatrix(5))
