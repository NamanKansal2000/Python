class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        for i in range(len(A)):
            max1 = max(A[i]+i, max1)
            min1 = min(A[i]+i, min1)
            max2 = max(A[i]-i, max2)
            min2 = min(A[i]-i, min2)

        return max(max1-min1, max2-min2)

A=[1, 3, -1]
s = Solution()
print(s.maxArr(A))
