
class Solution(object):
    def pathSum(self, root, sum):
        self.res = []
        if(root is None):
            return []
        self.dfs(root, [], 0, sum)
        return self.res

    def dfs(self, node, arr, s, sum):
        if(node.left is None and node.right is None and s+node.val == sum):
            arr2 = arr[:]
            arr2.append(node.val)
            self.res.append(arr2)
            return
        if(node.left):
            arr.append(node.val)
            self.dfs(node.left, arr, s+node.val, sum)
            arr.pop()
        if(node.right):
            arr.append(node.val)
            self.dfs(node.right, arr, s+node.val, sum)
            arr.pop()
