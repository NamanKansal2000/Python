class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        n = len(s)
        i = n-1
        while i >= 0:
            if s[i].isalpha():
                i-=1
            else:
                break
        return n-i-1
