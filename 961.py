class Solution(object):
    def repeatedNTimes(self, A):
        s = set()
        for v in A:
            if(v not in s):
                s.add(v)
            else:
                return v
