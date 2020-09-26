from typing import List
import math


class Solution:
    def isPowerOfThree(self, n: int):
        if n <= 0:
            return False
        a = math.log(n, 3)
        print(abs(a))
        return abs(a - int(a)) < 0.00000000009


a = Solution()
print(a.isPowerOfThree(243))
