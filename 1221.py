class Solution(object):
    def balancedStringSplit(self, s):
        count = ans = 0
        for S in s:
            count += -1 if(S == 'R') else 1
            if(count == 0):
                ans += 1
        return ans


a = Solution()
print(a.balancedStringSplit("RLRRLLRLRL"))
