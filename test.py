import re


class Solution(object):
    def isMatch(self, s, p):
        m = re.search(p, s)
        print(s, p)
        print(m.group())
        return s == m.group()


a = Solution()
# print(a.isMatch("aab", "c*a*b"))

b = 'abvcda'
print(sorted(b))
print(''.join(sorted(b)))
