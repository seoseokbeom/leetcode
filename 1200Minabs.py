# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr = sorted(arr)
#         res = []
#         mn = arr[-1]-arr[0]
#         bf = arr[-1]
#         for v in arr:
#             if abs(v-bf) < mn:
#                 res = [[bf, v]]
#                 mn = v-bf
#             elif v-bf == mn:
#                 res.append([bf, v])
#             bf = v
#         return res

class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        for a, b in zip(arr, arr[1:]):
            print(b - a)
        # print(mn)
        # return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]


a = Solution()
print(a.minimumAbsDifference([4, 2, 1, 3]))
