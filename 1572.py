class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]+mat[i][size-i-1]
        if(size % 2 == 1):
            sum -= mat[size//2][size//2]
        return sum

# class Solution(object):
#     def diagonalSum(self, mat):
#         sum = 0
#         size = len(mat)
#         i = 0
#         j = len(mat)-1
#         row = 0
#         while(i < size):
#             sum += mat[row][i]+mat[row][j]
#             row += 1
#             i += 1
#             j -= 1
#         if(size % 2 == 1):
#             sum -= mat[size//2][size//2]
#         return sum


a = Solution()
print(a.diagonalSum(mat=[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]))
