class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0
        small_len = min(len(a), len(b))
        big_len = max(len(a), len(b))
        arr = [a, b]
        for i, v in enumerate(arr):
            if len(arr[i]) == big_len:
                arr[i] = '0'+arr[i]
            else:
                arr[i] = '0'*(big_len-small_len+1) + arr[i]
        [a, b] = arr

        for i in range(big_len):
            sum_val = int(a[-1-i]) + int(b[-1-i])+carry
            if sum_val >= 2:
                carry = 1
            else:
                carry = 0
            res = str(sum_val % 2) + res
        if carry == 1:
            res = "1"+res
        return res


a = Solution()
print(a.addBinary(a="0", b="0"))
