from itertools import combinations


class Solution(object):
    def threeSumMulti(self, A, target):
        dic = dict()
        for v in A:
            if v in dic:
                dic[v] = dic[v]+1
            else:
                dic[v] = 1
        # print(list(dic.keys()))
        print(combinations(tuple(dic.keys()), 3))
        # for key, value in dic.items():

        # return dic


a = Solution()
print(a.threeSumMulti(A=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))
