class Solution(object):
    def defangIPaddr(self, address):
        a = address.split('.')
        return '[.]'.join(a)


a = Solution()
print(a.defangIPaddr("255.100.50.0"))
