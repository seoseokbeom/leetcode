class Solution(object):
    def increasingTriplet(self, nums):
        arr = [nums[0], nums[1]]
        for i, v in enumerate(nums):
            if v < arr[0]:
