class Solution:
    def sortByBits(self, A):
        return sorted(A, key=lambda x: [bin(x).count('1')])

        # dic = {}
        # for v in arr:
        #     a = (format(v, '0b').count('1'))
        #     if a in dic:
        #         dic[a].append(v)
        #     else:
        #         dic[a] = [v]
        # res = []
        # arr = []
        # for k, v in dic.items():
        #     arr.append((k, sorted(v)))
        # arr.sort(key=lambda x: x[0])
        # for v in arr:
        #     res.extend(v[1])
        # return res


a = Solution()
# print(a.sortByBits([10000, 10000]))
# print(a.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(a.sortByBits([10, 100, 1000, 10000]))
# print(a.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
