class Solution:
    def isHappy(self, n):
        vis = set()
        strnum = str(n)
        while strnum != '1' :
            print(vis)
            if strnum in vis:
                return False
            vis.add(strnum)
            tmp = 0
            for v in strnum:
                tmp += int(v)**2
            strnum = str(tmp)
        return True


a = Solution()
print(a.isHappy(19))
