class Solution(object):
    def finalPrices(self, prices):
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if(prices[i] >= prices[j]):
                    prices[i] = prices[i]-prices[j]
                    break
        return prices


class Solution(object):
    def finalPrices(self, A):
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]]


a = Solution()
print(a.finalPrices([10, 1, 1, 6]))
