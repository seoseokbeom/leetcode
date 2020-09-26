class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


a = Solution()
print(a.climbStairs(4))
