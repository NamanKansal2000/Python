class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):
        max_sum = arr[0]
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if max_sum < curr_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0
        return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(arr))
