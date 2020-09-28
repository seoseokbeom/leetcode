# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


TreeNode


class Solution(object):
    def widthOfBinaryTree(self, root):
        dic = defaultdict(list)

        def recursion(self, node, cnt, dic):
            if node is None:
                dic[cnt].append(None)
            else:
                dic[cnt].append(node.val)
                recursion(self, node.left, cnt+1, dic)
                recursion(self, node.right, cnt+1, dic)
        recursion(self, root, 0, dic)
        print(dic)
        max_dist = 0
        for arr in dic.values():
            print(arr)
            s = 0
            e = -1
            for i, v in enumerate(arr):
                if v != None:
                    s = i
                    break
            for i in range(len(arr)-1, -1, -1):
                if arr[i] != None:
                    e = i
                    break
            max_dist = max(max_dist, e-s+1)
        return max_dist


a = Solution()
print(a.widthOfBinaryTree())
