class Solution(object):
    def containsDuplicate(self, nums):
        vis = set()
        for v in nums:
            if v not in vis:
                vis.add(v)
            else:
                return True
        return False
