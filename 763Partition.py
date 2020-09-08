class Solution(object):
    def partitionLabels(self, S):
        dic = {c: i for i, c in enumerate(S)}
        arr = []
        left = 0
        right = 0
        print(dic)
        for i, c in enumerate(S):
            right = max(right, dic[c])
            if(right == i):
                arr.append(right-left+1)
                left = right+1
        return arr


a = Solution()
print(a.partitionLabels("ababcbacadefegdehijhklij"))
