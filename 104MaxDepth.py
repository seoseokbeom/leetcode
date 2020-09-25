# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        self.res = 0
        self.rec(root, 0)
        return self.res

    def rec(self, node, cnt):
        if node is None:
            self.res = max(self.res, cnt)
            return cnt
        # if node.left:
        self.rec(node.left, cnt+1)
    # if node.right:
        self.rec(node.right, cnt+1)
        # return max(a, b)
