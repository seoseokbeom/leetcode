class Solution(object):
    def maximum69Number(self, num):
        num = list(str(num))
        for i, s in enumerate(num):
            if(s == '6'):
                num[i] = '9'
                return int(''.join(num))
        return int(''.join(num))


class Solution(object):
    def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))


a = Solution()
print(a.maximum69Number(9999))
