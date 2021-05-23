class Solution:
    def maximumGap(self, A):
        if len(A) == 0 or len(A) == 1:
            return 0
        A = list(A)
        A.sort()
        max_diff = 0
        for i in range(len(A)-1):
            if A[i+1]-A[i] > max_diff:
                max_diff = A[i+1]-A[i]
        return max_diff

A = [1, 10, 5]
s = Solution()
print(s.maximumGap(A))
