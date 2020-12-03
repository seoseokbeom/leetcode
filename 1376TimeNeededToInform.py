class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        global res
        res = 0

        def find(idx, cost):
            if idx == headID:
                global res
                res = max(res, cost)
                return
            find(manager[idx], cost+informTime[manager[idx]])

        find(0, 0)
        return res


a = Solution()
print(a.numOfMinutes(n=7, headID=6, manager=[
      1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]))
