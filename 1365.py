class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                print(dct[n], i)
                dct[n] = i
        return [dct[n] for n in nums]


a = Solution()
print(a.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
