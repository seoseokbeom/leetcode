class Solution(object):
    def validPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                a=s[:i]+s[i+1:]
                b=s[:j]+s[j+1:]
                return a == a[::-1] or b == b[::-1]
            else:
                i += 1
                j -= 1
        return True


a = Solution()
print(a.validPalindrome('abca'))
