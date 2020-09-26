class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [0] * len(prices)
        s = prices[0]
        for i, v in enumerate(prices):
            s = min(s, v)
            if v > s:
                dp[i] = v-s
        return max(dp)


a = Solution()
print(a.maxProfit([]))
# print(a.maxProfit([7,1,5,3,6,4]))
# print(a.maxProfit( [7,6,4,3,1]))
