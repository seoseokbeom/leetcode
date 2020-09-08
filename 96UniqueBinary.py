class Solution(object):
    def numTrees(self, n):
        self.res = 0
        self.rec(0, 0, 0, n)
        return self.res

    def rec(self, left, right, cnt, n):
        if cnt == n-1:
            self.res += 1
            return
        if cnt > n-1:
            return
        self.rec(left+1, right, cnt+1, n)
        self.rec(left, right+1, cnt+1, n)
        self.rec(left+1, right+1, cnt+2, n)


a = Solution()
print(a.numTrees(4))
