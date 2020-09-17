class Solution(object):
    def arrangeCoins(self, n):
        return int((-1+(1+8*n)**0.5)/2)
