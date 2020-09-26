# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        stack = [root]
        while stack:
            elem = stack.pop()
            elem.right, elem.left = elem.left, elem.right
            stack.extend([elem.left, elem.right])
        return root
