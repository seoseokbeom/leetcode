class Solution:
    def reverseBits(self, n: int):
        res = ''
        while n:
            res += str(n % 2)
            n //= 2
        # print(len(res))
        res = '0'*(32-len(res)) + res
        res.reverse()
        return res


a = Solution()
print(a.reverseBits(999))
