class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = map(str, digits)
        return list(str(int(''.join(digits))+1))

        
