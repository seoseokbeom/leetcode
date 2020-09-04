class Solution(object):
    def sortArrayByParity(self, A):
        arr = []
        for i, v in enumerate(A):
            if(v % 2 == 0):
                arr.append(v)
        for i, v in enumerate(A):
            if(v % 2 != 0):
                arr.append(v)
        return arr


a = Solution()
print(a.sortArrayByParity([3, 1, 2, 4]))
# b = [3, 1, 2, 4]
# for v in b:
#     print(v)
