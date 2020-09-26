class Solution(object):
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = res*26 + ord(c)-64
        return res
