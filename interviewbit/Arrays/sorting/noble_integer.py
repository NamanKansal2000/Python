class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n-1):
            if A[i+1] == A[i]:
                continue
            if A[i] == n-1-i:
                return 1
        if A[n-1] == 0:
            return 1
        return -1

A = [3, 2, 1, 3]
s = Solution()
print(s.solve(A))
