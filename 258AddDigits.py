import math


class Solution(object):
    def addDigits(self, num):
        digit = num
        while digit >= 10:
            tmp = 0
            for i in range(int(math.log10(digit)) + 1):
                tmp += digit % 10
                digit = digit//10
            digit = tmp
        return digit


a = Solution()
print(a.addDigits(288))
