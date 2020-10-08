class Solution(object):
    def canConstruct(self, s, k):
        if len(s) < k:
            return False
        if len(s) == k:
            return True
