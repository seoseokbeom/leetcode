class Solution(object):
    def wordBreak(self, s, wordDict):
        queue = []
        visited = set()
        queue.append(s)
        while len(queue) != 0:
            sliced_s = queue.pop(0)
            if not sliced_s:
                return True
            for i, v in enumerate(wordDict):
                if sliced_s.find(v) == 0:
                    idx = len(v)
                    tmp = sliced_s[idx:]
                    if tmp not in visited:
                        queue.append(tmp)
                    visited.add(tmp)
        return False


a = Solution()
print(a.wordBreak("catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
