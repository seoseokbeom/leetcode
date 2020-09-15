class Solution(object):
    def countPrimes(self, n):
        dp = [True]*(n+1)
        for i in range(2, int(n**0.5)+1):
            if(dp[i]):
                # for j in range(i, n):
                #     if j*i > n:
                #         break
                dp[i*i:n:i] = [False] * len(dp[i*i:n:i])
                # if dp[i*j] is True:
                #     dp[i*j] = False
        res = 0
        res = sum(dp[2:n])
        # for i in range(2, n):
        #     if dp[i]:
        #         res += 1
        return res


a = Solution()
print(a.countPrimes(1500000))
