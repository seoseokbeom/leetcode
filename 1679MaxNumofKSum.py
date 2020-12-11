class Solution(object):
    def maxOperations(self, nums, k):
        sorting = sorted(nums)
        i, j = 0, len(nums)-1
        res = 0
        while i < j:
            if sorting[i]+sorting[j] == k:
                res += 1
                i += 1
                j -= 1
            elif sorting[i]+sorting[j] < k:
                i += 1
            else:
                j -= 1
        return res


a = Solution()
print(a.maxOperations(nums=[3, 1, 3, 4, 3], k=6
                      ))
