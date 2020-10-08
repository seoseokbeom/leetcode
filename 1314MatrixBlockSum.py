class Solution(object):
    def matrixBlockSum(self, mat, K):
        acc = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for a in range(len(mat)):
            for b in range(len(mat[0])):
                cnt = 0
                for i in range(a-K, a+K+1):
                    for j in range(b-K, b+K+1):
                        if i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0]):
                            cnt += mat[i][j]
                print(a, b, cnt)
                acc[a][b] = cnt
        return acc


a = Solution()
print(a.matrixBlockSum([[67, 64, 78], [99, 98, 38],
                        [82, 46, 46], [6, 52, 55], [55, 99, 45]], 3))
