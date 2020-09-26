from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        dic = defaultdict(lambda: 0)
        for v in nums:
            dic[v] += 1
        for key, value in dic.items():
            if val > len(nums)//2
            return key
