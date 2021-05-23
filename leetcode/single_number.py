class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*2) - (sum(nums))

###############################################################################
## Better Solution ############################################################
###############################################################################
# using XOR
# a^0 = a and a^a = 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a^=i
        return a
