class Solution:
    def flipAndInvertImage(self, A):
        for i, row in enumerate(A):
            A[i] = list(reversed(A[i]))
            for j, v in enumerate(A[i]):
                A[i][j] = 1 if v == 0 else 0
        return A


a = Solution()
print(a.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
