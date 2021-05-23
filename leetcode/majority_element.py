class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in nums:
            dict[i] = dict.get(i,0)+1
        for i,j in dict.items():
            if j > n//2:
                return i

###############################################################################
### Alternate Solution ###########################################################
###############################################################################

# Moore's voting algo

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = a[0]
        c = 1
        for i in range(1,len(nums)):
            if c == 0:
                val = a[i]
            if a[i] == val:
                c+=1
            else:
                c-=1
        return val
