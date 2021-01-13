# class Solution(object):
#     def maximalSquare(self, matrix):
#         dp = [[0 for _ in range(len(matrix[0])+1)]
#               for i in range(len(matrix)+1)]
#         w = 0
#         for i, row in enumerate(matrix):
#             for j, v in enumerate(row):
#                 if v == '1':
#                     dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
#                     w = max(w, dp[i+1][j+1])
#         return w*w


class Solution:
    def maximalSquare(self, A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = int(A[i][j])
                if i and j and A[i][j]:
                    A[i][j] = min(A[i-1][j], A[i][j-1], A[i-1][j-1])+1
        mx = A[0][0]
        for arr in A:
            mx = max(mx, max(arr))
        return mx**2


a = Solution()
print(a.maximalSquare(
    [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]))
