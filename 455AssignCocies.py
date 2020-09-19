class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        minlen = min(len(g), len(s))
        cnt = 0
        coockiesidx = 0
        for i, v in enumerate(g):
            # print(v, )
            if coockiesidx >= len(s):
                break
            if i == minlen:
                break
            while v > s[coockiesidx]:
                coockiesidx += 1
                if coockiesidx >= len(s):
                    break
            else:
                cnt += 1
                coockiesidx += 1
        return cnt


a = Solution()
print(a.findContentChildren(

    [10, 9, 8, 7],
    [5, 6, 7, 8]))
