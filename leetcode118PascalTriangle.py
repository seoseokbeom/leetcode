class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return [[]]
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[1] for _ in range(numRows)]
        res[1].append(1)
        for i in range(2, numRows):
            for j in range(i-1):
                print(res)
                tmp = res[i-1][j]+res[i-1][j+1]
                res[i].append(tmp)
            res[i].append(1)
        return res


a = Solution()
print(a.generate(0))
