class Solution(object):
    def xorOperation(self, n, start):
        res = 0
        for i in range(n):
            res ^= 2*i+start
        return res

a = Solution()
print(a.xorOperation(n = 10, start = 5))
