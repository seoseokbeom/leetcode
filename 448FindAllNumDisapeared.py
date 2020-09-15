class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        dp = [True] * (n+1)
        for v in nums:
            dp[v] = False
        return [i for i in range(1, n+1) if dp[i]]


a = Solution()
print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]
                               ))
