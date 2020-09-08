class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if(obstacleGrid is None or obstacleGrid[0][0] == 1):
            return 0

        arr = [[0 for col in range(len(obstacleGrid[0]))]
               for row in range(len(obstacleGrid))]
        arr[0][0] = 1
        for i in range(1, len(arr[0])):
            arr[0][i] = 1 if obstacleGrid[0][i] == 0 and arr[0][i-1] == 1 else 0
        for i in range(1, len(arr)):
            arr[i][0] = 1 if obstacleGrid[i][0] == 0 and arr[i-1][0] == 1 else 0
        for i in range(1, len(arr)):
            for j in range(1, len(arr[0])):
                if(obstacleGrid[i][j] == 1):
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i-1][j]+arr[i][j-1]
        return arr[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


a = Solution()
print(a.uniquePathsWithObstacles(
    [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
