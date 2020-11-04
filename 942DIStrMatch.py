class Solution(object):
    def diStringMatch(self, S):
        dc, ic = 0, 0
        for v in S:
            if v == "I":
                ic += 1
            else:
                dc += 1
        l, u = dc, dc+1
        res = [l]
        for v in S:
            if v == "I":
                res.append(u)
                u += 1
            else:
                l -= 1
                res.append(l)
        return res
