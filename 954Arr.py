import collections


class Solution(object):
    def canReorderDoubled(self, A):
        c = collections.Counter(A)
        print(c)
        print(sorted(c, key=abs))
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True


a = Solution()
print(a.canReorderDoubled([1, 2, 4, 16, 8, 4]))
