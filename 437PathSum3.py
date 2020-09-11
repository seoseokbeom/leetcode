# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        self.count = 0
        self.dfs(root, sum, 0)

    def dfs(self, node, sum, sum2):
        # if node is None:
        if sum == sum2:
            self.count += 1
        if node is None:
            return
        self.dfs(node.left, sum,  sum2+node.val)
        self.dfs(node.left, sum,  sum2)
        self.dfs(node.right, sum,  sum2+node.val)
        self.dfs(node.right, sum,  sum2)


a = Solution()
print(a.pathSum(root=[10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], sum=8))
