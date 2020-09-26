class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


a = Solution()
print(a.maxSubArray(nums=[-1, -2, 1, 2, 3, 4]))
