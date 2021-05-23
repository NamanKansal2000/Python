class Solution:
    def maximumGap(self, A):
        B = sorted(A)
        if B == A:
            return [-1]
        L = [i for i in range(len(A)) if A[i]!=B[i]]
        return [min(L), max(L)]

A= [1,6,3,2,4,5]
#  [1,2,3,4,5,6]
s = Solution()
print(s.maximumGap(A))
