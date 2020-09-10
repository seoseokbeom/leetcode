class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        dic = {}
        maxlen = 0
        if(len(s) == 0):
            return 0
        for i, v in enumerate(s):
            if dic.get(v) == None:
                maxlen = max(maxlen, i-left+1)
                dic[v] = i
            else:
                if left <= dic[v]:
                    maxlen = max(maxlen, i-left)
                    left = dic[v]+1
                else:
                    maxlen = max(maxlen, i-left+1)
                dic[v] = i
        return maxlen


a = Solution()
print(a.lengthOfLongestSubstring("tmmzuxt"))
