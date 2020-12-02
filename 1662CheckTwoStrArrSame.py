class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = str2 = ''
        for v in word1:
            str1 += v
        for v in word2:
            str2 += v
        return str1 == str2


a = Solution()
print(a.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))
