from typing import List


class Solution:
    def rob(self, nums: List[int]):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(dp[0]+nums[2], dp[1])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i])
        return dp[len(nums)-1]


a = Solution()
print(a.rob(nums=[0, 0, 0]))
