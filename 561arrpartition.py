class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res = 0
        for i, v in enumerate(nums):
            if i % 2 == 1:
                res += v
        return res
