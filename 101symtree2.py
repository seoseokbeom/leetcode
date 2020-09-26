# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode):
        return self.rec(root.left, root.right)

    def rec(self, ln, rn):
        if ln is None and rn is None:
            return True
        if ln is None or rn is None:
            return False
        return ln.val == rn.val and self.rec(ln.left, rn.right) and self.rec(ln.right, rn.left)
