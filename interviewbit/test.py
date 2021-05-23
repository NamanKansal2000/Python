class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        def RightSpecialValue(A, n):
            right = 0
            if n == len(A)-1:
                return 0
            right = max(A[n:len(A)])
            return right

        def LeftSpecialValue(A, n):
            left = 0
            if n == 0:
                return 0
            left = max(A[0:n])
            return left
        maxx = 0
        left = []
        right = []
        for i in range(len(A)):
            left.append(LeftSpecialValue(A, i))
            right.append(RightSpecialValue(A, i))
        print(left)
        print(right)
        le = max(left)
        r = max(right)
        maxx = le*r

        return maxx % 1000000007


obj = Solution()
A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
num = obj.maxSpecialProduct(A)
print(num)
