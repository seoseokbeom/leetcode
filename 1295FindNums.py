class Solution(object):
    def findNumbers(self, nums):
        res = 0
        for v in nums:
            res += 1 if len(str(v)) % 2 == 0 else 0
        return res
