
class Solution(object):
    def lowestCommonAncestor(self, node, p, q):
        if node in (None, p, q):
            return node
        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)
        if left and right:
            return node
        else:
            return left or right
