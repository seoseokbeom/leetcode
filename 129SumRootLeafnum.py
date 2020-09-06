
class Solution(object):
    def sumNumbers(self, root):
        self.sum = 0
        if root is None:
            return 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, num):
        print(num)
        if(node.left):
            self.dfs(node.left, num*10+node.val)
        if(node.right):
            self.dfs(node.right, num*10+node.val)
        if node.left is None and node.right is None:
            self.sum += num+node.val


a = Solution()
print(a.sumNumbers())
