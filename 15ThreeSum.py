class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        l = 0
        r = len(nums)-1
        m = l+1
        res = []
        while(r-l >= 2):
            sum = nums[l]+nums[m]+nums[r]
            if(sum == 0):
                res.append([nums[i], nums[m], nums[r]])
            elif sum < 0:
                m += 1
                if(m == r):
                    l += 1
                    m = l+1
                continue
            else:
                r -= 1
                m = l+1
            m += 1
            if m == r:
                l += 1
                m = l+1


a = Solution()
print(a.threeSum([-1, 0, 1, -11, 2, -1, -4]))
