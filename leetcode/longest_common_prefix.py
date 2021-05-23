class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        if n == 1:
            return strs[0]
        strs.sort()
        min_len = min(len(str[0]), len(strs[n-1]))
        i = 0
        while i < min_len and strs[0][i] == strs[n-1][i]:
            i+=1
        return strs[0:i]
