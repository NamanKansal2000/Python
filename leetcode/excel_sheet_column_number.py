class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        val = ord('A')
        for i in columnTitle:
            num = num*26+ord(i)-val+1
        return num
            
