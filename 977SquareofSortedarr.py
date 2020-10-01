class Solution:
    def sortedSquares(self, A):
        A = map(lambda x: x*x, A)
        return sorted(A)


a = Solution()
print(a.sortedSquares([-7, -3, 2, 3, 11]))
