class Solution:
    def repeatedNumber(self, A):
        dict = {}
        for i in A:
            if i not in dict.keys():
                dict[i] = 1
            else:
                return i
        return -1

A = [3,4,1,4,1]
s = Solution()
print(s.repeatedNumber(A))
