class Solution:
    def arrayRankTransform(self, A):
        D = {j: i+1 for i, j in enumerate(sorted(set(A)))}
        return map(D.get, A)


a = Solution()
print(a.arrayRankTransform([40, 10, 20, 30]))
