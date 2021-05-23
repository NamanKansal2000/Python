class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <5:
            return 0
        c = 0
        if n == 5:
            return 1
        while n >= 5:
            c += n//5
            n = n // 5
        return c
