from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        dic = Counter(nums1)
        print(dic)
        res = []
        for v in nums2:
            # print(v, dic[v])
            if dic[v] > 0:
                res += v,
                dic[v] -= 1
        return res


a = Solution()
print(a.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
