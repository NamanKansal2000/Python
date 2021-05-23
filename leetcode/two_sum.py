class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            mat = target - j
            if mat in (rest:=nums[(i+1):]):
                index = rest.index(mat)
                return [i, index+i+1]
