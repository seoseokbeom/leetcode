class Solution(object):
    def maximalSquare(self, matrix):
        dp = [[0 for _ in range(len(matrix[0])+1)]
              for i in range(len(matrix)+1)]
        print(dp)
        w = 0
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
                    w = max(w, dp[i+1][j+1])
        print(dp)
        return w*w


a = Solution()
print(a.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
      "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
