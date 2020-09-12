class Solution(object):
    def dfs(self, grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
            return
        if(grid[i][j] == '1'):
            grid[i][j] = '0'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

    # def numIslands(self, grid):
    #     cnt = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if(grid[i][j] == '1'):
    #                 self.dfs(grid, i, j)
    #                 cnt += 1
    #     return cnt

    def numIslands(self, grid):
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == '1'):
                    self.bfs(grid, i, j)
                    cnt += 1
        return cnt

    def bfs(self, grid, i, j):
        queue = []
        queue.append((i, j))
        grid[i][j] = '0'
        while(len(queue)):
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            i, j = queue.pop(0)
            for d in dir:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '1':
                    queue.append((ni, nj))
                    grid[ni][nj] = '0'


a = Solution()
print(a.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
