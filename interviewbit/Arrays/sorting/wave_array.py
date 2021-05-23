class Solution:
    def wave(self, A):
        A.sort() # because output required in lexographical order
        n = len(A)
        if len(A)== 0 or len(A) == 1:
            return A
        if len(A) == 2:
            if A[0] < A[1]:
                A[0], A[1] = A[1], A[0]
        for i in range(0, n, 2):
            if i > 0 and A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]
            if i < n-1 and A[i+1] > A[i]:
                A[i+1], A[i] = A[i], A[i+1]

A = [1,2,3,4]
s = Solution()
print(s.wave(A))
