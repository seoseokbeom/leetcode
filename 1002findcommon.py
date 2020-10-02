from collections import Counter


class Solution:
    def commonChars(self, A):
        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
            print(res)


a = Solution()
print(a.commonChars(["bbbbb", "bbb", "bb"]))


print((5 & 10))
