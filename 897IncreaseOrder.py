
class Solution:
    def increasingBST(self, root):
        self.res = []
        self.recursion(root)
        return self.res

    def recursion(self, node):
        if node is None:
            return
        if node.left:
            self.recursion(node.left)
            self.res.append(node.left.val)
        if node.right:
            self.recursion(node.right)
            self.res.append(node.right.val)


a = Solution()
print(a.increasingBST())
