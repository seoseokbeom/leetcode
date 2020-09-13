class Solution(object):
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val >= ceiling or root.val <= floor:
            return False
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)