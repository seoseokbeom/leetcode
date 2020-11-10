class Solution(object):
    def findCircleNum(self, M):
        sets = [i for i in range(len(M))]

        def find(x):
            if x == sets[x]:
                return x
            sets[x] = find(sets[x])
            return sets[x]

        for j in range(0, len(M)):
            for i in range(j+1, len(M)):
                if M[i][j] == 1:
                    sets[find(i)] = find(j)

        return sum([1 for i, v in enumerate(sets) if i == v])

        # res = 0
        # for i, v in enumerate(sets):
        #     if v == i:
        #         res += 1
        # return res


a = Solution()
print(a.findCircleNum([[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [
      1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]))
