class Solution:
    def flip(self, A):
        curr_sum = 0
        max_sum = 0
        start = 0
        end = 0
        poi = 0
        ans =None
        for i, a in enumerate(A):
            curr_sum += (1 if a == '0' else -1)
            if curr_sum > max_sum:
                max_sum = curr_sum
                start = poi
                end = i
                ans = [start, end]
            if curr_sum < 0:
                curr_sum = 0
                poi = i+1
        if ans is None:
            return []
        return list(map(lambda x:x+1, ans))

A = '010'
s = Solution()
print(s.flip(A))
