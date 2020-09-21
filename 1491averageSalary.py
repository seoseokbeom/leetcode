class Solution(object):
    def average(self, salary):
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)


a = Solution()
print(a.average([48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000,
                 37000, 93000, 77000, 33000, 28000, 4000, 54000, 67000, 6000, 1000, 11000]))
