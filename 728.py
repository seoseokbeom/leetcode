class Solution(object):
    def selfDividingNumbers(self, left, right):
        arr = []
        for i in range(left, right+1):
            if(self.selfd(i)):
                arr.append(i)
        return arr

    def selfd(self, n):
        s = str(n)
        for i in range(len(s)):
            if(s[i] == '0' or n % int(s[i]) != 0):
                return False
        return True


a = Solution()
print(a.selfDividingNumbers(left=1, right=22))
