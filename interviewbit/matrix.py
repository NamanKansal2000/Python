class Solution:
    def spiral(self, A):
        n = len(A)
        top, bottom = 0, n-1
        left, right = 0, n-1
        row, col = 0, 0
        direction = 0
        ls = []
        while(left <= right and top <= bottom):
            if direction == 0:
                for col in range(left, right + 1):
                    ls.append(A[row][col])
                top += 1
            if direction == 1:
                for row in range(top, bottom + 1):
                    ls.append(A[row][col])
                right -= 1
            if direction == 2:
                for col in reversed(range(left, right+1)):
                    ls.append(A[row][col])
                bottom -= 1
            if direction == 3:
                for row in reversed(range(top, bottom + 1)):
                    ls.append(A[row][col])
                left += 1
            direction = (direction + 1) % 4
        return ls

    def rotate_90_clockwise(self, A, deg):
        deg = (deg // 90) % 4
        for count in range(deg):
            for i in range(len(A)):
                for j in range(i, len(A)):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
            n = len(A)
            for i in range(n):
                for j in range(n//2):
                    A[i][j], A[i][n-1-j] = A[i][n-1-j], A[i][j]
        return A

    def move_r(self, A, r):
        for count in range(r):
            top, bottom = 0, len(A) - 1
            left, right = 0, len(A) - 1
            while left <= right and top <= bottom:
                prev = A[top + 1][left]
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
                for i in reversed(range(left, right + 1)):
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

    def transpose(self, A):
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A


obj = Solution()
A = 80
B = [[0 for i in range(A)]for j in range(A)]
c = 1
for i in range(A):
    for j in range(A):
        B[i][j] = c
        c += 1
for i in range(len(B)):
    print(B[i])
val = obj.rotate_90_clockwise(B,180)
for i in range(len(B)):
    print(val[i])
