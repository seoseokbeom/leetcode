class Solution(object):
    def singleNumber(self, nums):
        dic = set()
        for v in nums:
            if v not in dic:
                dic.add(v)
            else:
                dic.remove(v)
        return dic.pop()
