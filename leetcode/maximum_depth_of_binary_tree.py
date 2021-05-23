# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            ld = maxDepth(root.left)
            rd = maxDepth(root.right)
            if ld < rd:
                return ld+1
            else:
                return rd+1
