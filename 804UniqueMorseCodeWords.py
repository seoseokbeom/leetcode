class Solution(object):
    def uniqueMorseRepresentations(self, words):
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
               "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        ans = ''
        for word in words:
            for char in word:
                ans += arr[ord(char)-97]
            res.add(ans)
            ans = ''
        return res


# print(ord('a')-97)
a = Solution()
print(a.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))
