class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count


a = Solution()
print(a.busyStudent(startTime=[9, 8, 7, 6, 5, 4, 3, 2, 1], endTime=[
      10, 10, 10, 10, 10, 10, 10, 10, 10], queryTime=5))
