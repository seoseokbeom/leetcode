class Solution(object):
    def missingNumber(self, nums):
        dp = [0]*(len(nums)+1)
        for v in nums:
            dp[v]=1
        return dp.index(0)


a=Solution()
print(a.missingNumber([3,0,1]))