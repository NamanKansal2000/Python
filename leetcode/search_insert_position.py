class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        i = 1
        n = len(nums)
        lp = 0
        while i < n and nums[i] < target:
            lp = i
            i = i * 2
        if i < n and nums[i] == target:
            return i
        while lp < n and nums[lp] < target:
            lp+=1
        if lp < n and nums[lp] == target:
            return lp
        return lp

        
