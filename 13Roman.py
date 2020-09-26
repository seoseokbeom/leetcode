class Solution(object):
    def romanToInt(self, s):
        dic = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        print(dic['x'])
        res = 0
        for i, c in enumerate(s):
            if s[i]
        for c in s:
            res += dic[c]
        return res


a = Solution()
print(a.romanToInt('IV'))
