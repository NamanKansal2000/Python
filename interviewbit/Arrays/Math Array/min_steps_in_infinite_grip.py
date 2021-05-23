class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        n = len(A)
        count = 0
        if n == 1 or n == 0:
            return 0
        for i in range(n-1):
            count+=max(abs(A[i+1]-A[i]), abs(B[i+1]-B[i]))
        return count


"""
Testing Code
"""
A = [0, 1, 1]
B = [0, 1, 2]
s = Solution()
print(s.coverPoints(A,B))
