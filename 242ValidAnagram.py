from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str):
        dic1 = Counter(s)
        dic2 = Counter(t)
        return dic1 == dic2


def reverseBits(n: int):
    return format(n, '032b')


a = 'abcde'
print(''.join(reversed(a)))
print(a[::-1])

# print(reverseBits(10))

# a = Solution()
# print(a.isAnagram(s="anagram", t="nagaram"))
