class Solution(object):
    def removeOuterParentheses(self, S):
        i = 0
        ans = ''
        S = list(S)
        print(S)
        mark = 0
        count = 0
        for i, s in enumerate(S):
            if(mark == 0 and s == '('):
                mark += 1
                print(i, 'first')
                S[i] = ''

            else:
                if(s == '('):
                    count += 1
                else:
                    count -= 1
                if(count < 0):
                    mark -= 1
                    print(i)
                    S[i] = ''
                    count = 0
        S = ''.join(S)
        print(S)
        return ans


a = Solution()
print(a.removeOuterParentheses("(()())(())"))
