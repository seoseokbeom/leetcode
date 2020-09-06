
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        sum -= root.val
        return self.hasPathSum(root.left) or self.hasPathSum(root.right)
