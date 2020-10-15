class Solution:
    def findComplement(self, num: int):
        n = num
        res = 0
        cnt = 0
        while n:
            n, r = divmod(n, 2)
            i = 1 ^ r
            res = res + i*(2**cnt)
            cnt += 1
        return res


a = Solution()
print(a.findComplement(1))
