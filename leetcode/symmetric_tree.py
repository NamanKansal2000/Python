# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return traverse(p.left, q.right) and traverse(p.right, q.left)
            else:
                return False
        return(traverse(root.left, root.right))
