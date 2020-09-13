
class Solution(object):
    def lowestCommonAncestor(self, node, p, q):
        if p == node or q == node:
            return node
        if not node:
            return None
        left = self.lowestCommonAncestor(node.left, p, q)
        right = self.lowestCommonAncestor(node.right, p, q)
        if left and right:
            return node
        else:
            return left or right
