class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n%2
            n//=2
        return res



a=Solution()
print(a.hammingWeight(11))