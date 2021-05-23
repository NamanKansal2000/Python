class Solution:

    def _first_greater(self, A, prev=True):
        ls, ans = list(), [0] * len(A)

        val = range(len(A)) if prev else range(len(A)-1, -1, -1)

        for i in val:
            while ls and A[i] >= A[ls[-1]]:
                ls.pop()
            ans[i] = ls[-1] if ls else 0
            ls.append(i)
        return ans

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        print(left)
        print(right)
        maxx = -float('inf')

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)

        return maxx % 1000000007


obj = Solution()
A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]
num = obj.maxSpecialProduct(A)
print(num)
