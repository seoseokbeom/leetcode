class Solution:
    def islandPerimeter(self, grid) -> int:
        for i, arr in enumerate(grid):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid.insert(0, [0 for _ in range((len(grid[0])))])
        grid.append([0]*(len(grid[1])))
        cnt = 0
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    for d in direct:
                        (tmpi, tmpj) = (i+d[0], j+d[1])
                        if grid[tmpi][tmpj]:
                            cnt += 1
        numNode = 0
        for row in grid:
            numNode += sum(row)
        return 4*numNode-cnt


a = Solution()
print(a.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
