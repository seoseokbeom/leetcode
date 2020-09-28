class Solution(object):
    def subsets(self, nums):
        self.res = []
        self.recursion(nums, 0, [])
        return self.res

    def recursion(self, nums, i, arr):
        if i >= len(nums):
            self.res.append(arr)
            return
        tmp1 = arr.copy()
        self.recursion(nums, i+1, tmp1)
        tmp2 = arr.copy()
        tmp2.append(nums[i])
        self.recursion(nums, i+1, tmp2)


a = Solution()
print(a.subsets([1, 2, 3]))
