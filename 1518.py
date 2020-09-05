class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        full = numBottles
        remain = numBottles
        ans = numBottles
        while(full >= numExchange):
            before_bottle = full
            full = full//numExchange
            remain = before_bottle-(full)*numExchange
            remain = remain+full
            ans += full
            full = remain
        return ans


a = Solution()
print(a.numWaterBottles(numBottles=9, numExchange=3
                        ))
