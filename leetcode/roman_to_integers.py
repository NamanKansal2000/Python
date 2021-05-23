class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900, 'I':1, 'V':5, 'X':10,'C':100, 'L':50, 'D':500, 'M':1000}
        sum = 0
        i = 0
        n = len(s)
        while i < n-1:
            val = s[i]+s[i+1]
            if val in d:
                sum+=d[val]
                i+=2
            else:
                sum += d[s[i]]
                i+=1
        if i == n-1:
            sum+=d[s[n-1]]
        return sum
