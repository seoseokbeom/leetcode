class Solution(object):
    def thousandSeparator(self, n):
        string = str(n)
        ans = ""
        while(string and len(string)):
            if(len(string) > 3):
                ans = '.' + string[-3:] + ans
            else:
                ans = string[-3:] + ans
            string = string[:-3]
            # print(ans, string)
        return ans


a = Solution()
print(a.thousandSeparator(0))
