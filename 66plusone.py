class Solution:
    def plusOne(self, digits):
        c = 0
        for i in range(len(digits)-1, -1, -1):
            tmp=c
            if i == len(digits)-1:
                c = (digits[i]+1+tmp)//10
                digits[i] = (digits[i]+1+tmp) % 10
            else:
                c = (digits[i]+tmp)//10
                digits[i] = (digits[i]+tmp) % 10

        if c == 1:
            digits.insert(0, 1)
        return digits


a = Solution()
print(a.plusOne(digits=[]))
