import random
import string


def solution(s):
    res = 0
    cnt = 0
    # dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for j in range(len(s)):
        cnt = 1
        mid = -1
        for i in range(j+1, len(s)):
            if s[j] != s[i]:
                if mid == -1:
                    mid = i
                dp[i][j] = i-j
            else:
                if mid == -1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i-1][j], i-mid)
    return sum(sum(row) for row in dp)

    # dp[i][j] = max()
    # if s[i] == s[i-1]:
    #     cnt += 1
    #     dp[i][j] = 0 if dp[i-1][j] == 0 else max(dp[i-1][j], cnt)
    # else:
    #     cnt = 1
    #     dp[i][j] = dp[i-1][j]
    # for row in dp:
    #     print(row)

# res += far(s[j:i])
# return res


def solution2(s):
    res = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res += far(s[i:j])
    return res


def far(s):
    i, j, k = 0, len(s)-1, 0
    cnt = 0
    while k <= len(s)-1:
        if s[i] != s[j-k] or s[i+k] != s[j]:
            return j-i-k
        else:
            k += 1
    return 0

# def far(s):
#     i, j, k = 0, len(s)-1, 0
#     cnt = 0
#     while k <= len(s)-1:
#         if s[i] != s[j-k] or s[i+k] != s[j]:
#             return j-i-k
#         else:
#             k += 1
#     return 0


#     print(s[i:j], far(s[i:j]))

#     if(s[i] != s[j]):
#         return j-i
def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))


# print(solution('pkwpp'))
# print(solution2('pkwpp'))
# print(solution('babaa'))
# print(solution2('babaa'))
print(solution('bbbaaababaaab'))
print(solution2('bbbaaababaaab'))

for _ in range(100):
    test = random_char(10)
    if solution(test) != solution2(test):
        print(solution(test))
        print(solution2(test))
        print(test)
        print()
# print(solution("oo"	))
