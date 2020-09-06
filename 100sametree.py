
class Solution(object):
    def isSameTree(self, p, q):
        if(p and q):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if(p == None and q == None):
            return True
        elif (p or q):
            return False
        if(q.val == p.val):
            return True
        return False
