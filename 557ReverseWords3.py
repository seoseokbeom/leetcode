class Solution:
    def reverseWords(self, s: str) -> str:
        print(s.split()[::-1])
        print(' '.join(s.split()[::-1])[::-1])
        arr = s.split()
        for i, v in enumerate(arr):
            arr[i] = v[::-1]
        return ' '.join(arr)


a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))
