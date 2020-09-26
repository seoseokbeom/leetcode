class Solution(object):
    def reverseString(self, s):
        print(s[::-1])
        s = s[::-1]
        print(s)


a = Solution()
print(a.reverseString(["h", "e", "l", "l", "o"]))
