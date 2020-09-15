class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        res = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        res += 1
        return res

    def calc(self, arr, i, j, k, a1, b1, c1):
        a = abs(arr[i]-arr[j]) <= a1
        b = abs(arr[j]-arr[k]) <= b1
        c = abs(arr[i]-arr[k]) <= c1
        return a and b and c


a = Solution()
print(a.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
