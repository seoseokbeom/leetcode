class Solution:
    def kWeakestRows(self, mat, k):
        arr = []
        for i, row in enumerate(mat):
            arr += (sum(row), i),
        arr.sort(key=lambda x: x[0])
        print(arr)
        return [arr[i][1] for i in range(k)]


a = Solution()
print(a.kWeakestRows(mat=[[1, 0, 0, 0],
                          [1, 1, 1, 1],
                          [1, 0, 0, 0],
                          [1, 0, 0, 0]],
                     k=2))
