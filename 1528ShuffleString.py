class Solution(object):
    def restoreString(self, s, indices):
        ans = ['']*len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return ''.join(i for i in ans)


a = Solution()
print(a.restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]))
