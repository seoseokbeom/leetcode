class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_str = set(allowed)
        cnt = 0
        for string in words:
            for i, v in enumerate(string):
                if v not in allowed_str:
                    break
                if i == len(string)-1 and v in allowed_str:
                    cnt += 1
        return cnt


a = Solution()
print(a.countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]
                               ))
