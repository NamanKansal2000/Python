# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1+self.minDepth(root.right)
        if root.right == None:
            return 1+self.minDepth(root.left)
        else:
            ld = self.minDepth(root.left)
            rd = self.minDepth(root.right)
            if ld > rd:
                return rd+1
            else:
                return ld+1
###############################################################################
## ####################### Better Solution ####################################
###############################################################################
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = []

        q.append({'node': root , 'depth' : 1})
        while len(q)>0:
            val = q.pop(0)
            node = val['node']
            depth = val['depth']
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                q.append({'node' : node.left , 'depth' : depth+1})
            if node.right is not None:
                q.append({'node': node.right , 'depth' : depth+1})
