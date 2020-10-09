class Solution:
    def reverseString(self, s):
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)


a = Solution()
print(a.reverseString(["h", "e", "l", "l", "o"]))
