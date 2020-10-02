class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        res = []
        mn = arr[-1]-arr[0]
        bf = arr[-1]
        for v in arr:
            if abs(v-bf) < mn:
                res = [[bf, v]]
                mn = v-bf
            elif v-bf == mn:
                res.append([bf, v])
            bf = v
        return res
