class Solution(object):
    def decompressRLElist(self, nums):
        freq = 0
        arr = []
        for i, v in enumerate(nums):
            if i % 2 == 0:
                freq = nums[i]
            else:
                arr.extend(([nums[i]]*freq))
        return arr


a = Solution()
print(a.decompressRLElist([1, 1, 2, 3]))
