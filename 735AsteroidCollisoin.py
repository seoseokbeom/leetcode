class Solution(object):
    def asteroidCollision(self, asteroids):
        self.res = []
        self.visited = set()
        self.recursion(asteroids, 0)
        return self.res

    def recursion(self, arr, idx):
        s = None
        if (tuple(arr), idx) in self.visited:
            return
        else:
            self.visited.add((tuple(arr), idx))
        mark = 0
        for i, v in enumerate(arr):
            if s and s > 0 and v < 0:
                if abs(s) < abs(v):
                    self.recursion(arr[:i-1]+arr[i:], i-1)
                elif abs(s) == abs(v):
                    self.recursion(arr[:i-1] + arr[i+1:], i-1)
                else:
                    self.recursion(arr[:i]+arr[i+1:], i)
                mark = 1
            s = v
        if len(arr) < 2 or mark == 0:
            self.res = arr


a = Solution()
print(a.asteroidCollision([3, -69, -65, 67, -76, 34, 10, 96, 55, 77, 85, 56, 99, -1, 6, -37, -7, -70, 75, -60, 4, -73, 35, -32, 3, -7, 72, 83, -82, 70, 68, 63, 33, -68, -100, 61, -96, 27, 89, 81, -11, -63, 69, 49, -34, 23, 87, 23, 26, -67, 67, -100, -84, -89, -76, -42, -86, -96, 86, 7, 25, 9, -17, 7, -15, -35, -65, -82, -32, 90, -27, 39, 30, -42, -3, -71, -46, 24, 20, -84, 8, 51, -84, 24, 53, 66, 87, -64, 27, -5, -68, 86, -49, -53, 68, 21, -88, 58, 21, -18]
                          ))
