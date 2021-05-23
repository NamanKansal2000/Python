class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return
        l1 = m - 1
        l2 = n - 1
        last = m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[last] = nums1[l1]
                l1 -= 1
                last -= 1
            else:
                nums1[last] = nums2[l2]
                l2 -= 1
                last -= 1

        while l2 >= 0:
            nums1[last] = nums2[l2]
            l2 -= 1
            last -= 1
