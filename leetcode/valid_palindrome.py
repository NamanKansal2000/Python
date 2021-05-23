class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for i in s:
            if i.isalnum():
                a+=i.lower()
        return a == a[::-1]
        
