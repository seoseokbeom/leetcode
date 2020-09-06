class Solution(object):
    def minCost(self, s, cost):
        sum = 0
        i = 1
        bi = 0
        while(i < len(s)):
            if(s[bi] == s[i]):
                if(cost[bi] < cost[i]):
                    sum += cost[bi]
                    bi = i
                else:
                    sum += cost[i]
            else:
                bi = i
            i += 1
        return sum


a = Solution()
print(a.minCost(
    "aaabbbabbbb",
    [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
