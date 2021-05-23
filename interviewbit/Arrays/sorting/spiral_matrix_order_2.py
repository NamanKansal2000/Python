class Solution:
    def matrix(self, A):
        arr = [[0 for i in range(A)] for i in range(A)]
        count = 0
        top, bottom = 0, A-1
        left, right = 0, A-1
        row, col = 0, 0
        direction = 0
        while top <= bottom and left<= right:

            for col in range(left, right+1):
                count += 1
                arr[row][col] = count
            top+=1

            for row in range(top,bottom+1):
                count+=1
                arr[row][col] = count
            right-=1

            for col in range(right, left-1, -1):
                count+=1
                arr[row][col] = count
            bottom-=1

            for row in range(bottom, top-1, -1):
                count+=1
                arr[row][col] = count
            left+=1

        return arr



A = 8
s = Solution()
val = s.matrix(A)
for i in val:
    print(i)
