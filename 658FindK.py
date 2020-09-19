class Solution(object):
    def findClosestElements(self, arr, k, x):
        # idx = len(arr)-1
        l = r = -1
        for i, v in enumerate(arr):
            if v == x:
                # idx = i
                l = i-1
                r = i
                break
            elif v > x:
                r = i
                l = i-1
                break
        # print(l, r)
        res = []
        while k != 0 and (l >= 0 or r < len(arr)):
            print(l, r, 'k', k)
            if r >= len(arr):
                res.insert(0, arr[l])
                l -= 1
            elif l < 0 :
                res.append(arr[r])
                r += 1
            elif abs(arr[r]-x) >= abs(arr[l]-x):
                res.insert(0, arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            print(res)
            k -= 1
        return res


a = Solution()
# print(a.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
print(a.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
