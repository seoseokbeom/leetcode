class Solution(object):
    def convertToBase7(self, num):
        tmp = abs(num)
        res = ''
        # print((1)//7)
        if tmp == 0:
            return '0'
        while tmp != 0:
            res = str(tmp % 7)+res
            tmp = tmp//7
        if num < 0:
            res = '-'+res
        return res


a = Solution()
# print(a.convertToBase7(100))
print(a.convertToBase7(-700))
