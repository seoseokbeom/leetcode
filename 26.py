class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)


a = Solution()
print(a.removeDuplicates([1, 1, 2]))


a = [1, 2, 3, 4]
b[:] = a
c = []
c[:] = a
a[0] = 999
print(b)
print(c)
