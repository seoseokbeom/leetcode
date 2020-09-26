class Solution:
    def countAndSay(self, n: int):
        if n == 1:
            return '1'
        dp = ['']*(n+1)
        dp[1] = '1'
        for i in range(2, n+1):
            cnt = 1
            tmp = dp[i-1]+'s'
            tmpres = ''
            for j in range(1, len(tmp)):
                if tmp[j-1] == tmp[j]:
                    cnt += 1
                else:
                    tmpres += str(cnt)+tmp[j-1]
                    cnt = 1
            dp[i] = tmpres
        return dp[n]


a = Solution()
print(a.countAndSay(5))
