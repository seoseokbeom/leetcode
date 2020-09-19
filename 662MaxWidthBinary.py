# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution(object):
    def widthOfBinaryTree(self, root):
        dic = defaultdict(list)

        def recursion(self, node, cnt, dic):
            if node is None:
                dic[cnt].append(None)
            else:
                dic[cnt].append(node.val)
        recursion(self, root, 0, dic)
        print(dic)
        max_dist = 0
        for arr in dic:
            s = 0
            e = -1
            for i, v in enumerate(arr):
                if v != None:
                    s = v
                    break
            for i in range(len(arr)-1, -1, -1):
                if arr[i] != None:
                    e = arr[i]
                    break
            max_dist = max(max_dist, e-s+1)
        return max_dist


a = Solution()
print(a.widthOfBinaryTree())
