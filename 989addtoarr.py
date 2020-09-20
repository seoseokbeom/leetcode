class Solution(object):
    def addToArrayForm(self, A, K):
        newarr = []
        for a in A:
            newarr.append(str(a))
        strnum = ''.join(newarr)
        res = (K+int(strnum))
        newarr = []
        for i in range(len(str(res))):
            newarr.insert(0, res % 10)
            res = res//10
        return newarr


a = Solution()
print(a.addToArrayForm(A=[2, 7, 4], K=181))
