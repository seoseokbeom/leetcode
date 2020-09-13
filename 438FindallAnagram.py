class Solution(object):
    def findAnagrams(self, s, p):
        dic = {}
        if(len(s) < len(p)):
            return []
        for v in p:
            if not dic.get(v):
                dic[v] = 1
            else:
                dic[v] = dic[v]+1
        for i, v in enumerate(s):
            if(i >= len(p)):
                break
            if not dic.get(v):
                dic[v] = -1
            elif dic.get(v) == 1:
                del dic[v]
            else:
                dic[v] = dic[v]-1
        arr = []
        for i, v in enumerate(s):
            if not len(dic):
                arr.append(i)
            if not dic.get(v):
                dic[v] = 1
            elif dic[v] == -1:
                del dic[v]
            else:
                dic[v] = dic[v]+1
            if(i+len(p) >= len(s)):
                break
            if not dic.get(s[i+len(p)]):
                dic[s[i+len(p)]] = -1
            elif dic.get(s[i+len(p)]) == 1:
                del dic[s[i+len(p)]]
            else:
                dic[s[i+len(p)]] = dic[s[i+len(p)]]-1
        return arr


a = Solution()
print(a.findAnagrams("abab",
                     "ab"))
