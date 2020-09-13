
class Solution(object):
    def isSameTree(self, p, q):
        if(p and q):
            return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if(p == None and q == None):
            return True
        return False
