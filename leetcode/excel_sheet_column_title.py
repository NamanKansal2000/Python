class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber > 0:
            val = (columnNumber-1)%26
            s += chr(val + ord('A'))
            columnNumber = (columnNumber-1)//26
        return s[::-1]
