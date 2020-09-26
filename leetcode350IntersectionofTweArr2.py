from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        dic = Counter(nums1)
        print(dic)
        res = []
        for v in nums2:
            print(v, dic[v])
            if dic[v] > 0:
                res.append(v)
                dic[v] -= 1
        return res

        # class Solution(object):
        #     def intersect(self, nums1, nums2):
        #         nums1.sort()
        #         nums2.sort()
        #         cnt = 0
        #         i = j = 0
        #         res=[]
        #         while i < len(nums1) or j < len(nums2):
        #             if i >= len(nums1):
        #                 j += 1
        #             elif j >= len(nums2) or nums1[i] < nums2[j]:
        #                 i += 1
        #             elif nums1[i] == nums2[j]:
        #                 res.append(nums1[i])
        #                 cnt += 1
        #                 i += 1
        #                 j += 1
        #             else:
        #                 j += 1
        #         return res


a = Solution()
print(a.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
