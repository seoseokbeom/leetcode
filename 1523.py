class Solution(object):
    def countOdds(self, low, high):
        if((high-low+1) % 2 == 0):
            return (high-low+1)//2
        else:
            return (high-low+1)//2 + (1 if low % 2 == 1 else 0)


a = Solution()
print(a.countOdds(8, 10))
