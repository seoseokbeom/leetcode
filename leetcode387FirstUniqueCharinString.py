from collections import defaultdict


class Solution(object):
    def firstUniqChar(self, s):
        dic = defaultdict(lambda: 0)
        for i, v in enumerate(s):
            dic[v] += 1
        for k, v in dic.items():
            if v == 1:
                return s.find(k)


a = Solution()
print(a.firstUniqChar(s="loveleetcode"

                      ))
