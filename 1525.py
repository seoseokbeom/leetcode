class Solution:
    def numSplits(self, s: str) -> int:
        p, total = set(), collections.Counter(s)
        res, total_cnt = 0, len(total)
        for i, x in enumerate(s[::-1]):
            p.add(x)
            total[x] -= 1
            total_cnt -= not total[x]
            res += len(p) == total_cnt
        return res


a = Solution()
print(a.numSplits("aacaba"))
