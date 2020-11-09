class Solution(object):
    def findRedundantConnection(self, edges):
        sets = [0] * (len(edges)+1)

        def find(x):
            if sets[x] == 0:
                return x
            return find(sets[x])

        for x, y in edges:
            u = find(x)
            v = find(y)
            if u == v:
                return [x, y]
            sets[u] = v


a = Solution()
print(a.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
