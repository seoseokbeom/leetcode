
class Solution(object):
    def isSymmetric(self, root):
        if(root == None):
            return True
        return self.sym(root.left, root.right)

    def sym(self, a, b):
        if(a and b):
            return a.val == b.val and self.sym(a.left, b.right) and self.sym(a.right, b.left)
        return a is b
