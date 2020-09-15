class Solution(object):
    def findUnsortedSubarray(self, nums):
        sort_arr = sorted(nums)
        start, end = 0, -1
        for i, v in enumerate(nums):
            if v != sort_arr[i]:
                start = i
                break
        for i in range(len(nums)-1, -1, -1):
            if sort_arr[i] != nums[i]:
                end = i
                break
        return end-start+1


a = Solution()
print(a.findUnsortedSubarray([1, 2, 3, 4]

                             ))
