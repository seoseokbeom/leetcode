class Solution(object):
    def intersection(self, nums1, nums2):
        a1 = set(nums1)
        a2 = set(nums2)
        return list(a1.intersection(a2))


a = Solution()
print(a.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
