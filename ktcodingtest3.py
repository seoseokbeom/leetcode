from random import randint


def solution(A):
    dp = [0 for _ in range(len(A)+1)]
    dp[0] = 1
    for v in A:
        dp[v] += 1
    i, j = 1, 1
    # i for finding 0, j for finding val>1
    cnt = 0
    # print(dp)
    while i < len(dp) and j < len(dp):
        while i < len(dp) and dp[i] != 0:
            i += 1
        while j < len(dp) and dp[j] <= 1:
            j += 1
        # print(i, j, cnt)
        if i >= len(dp) and j >= len(dp):
            break
        if i == len(dp) or j == len(dp):
            return -1
        cnt += abs(i-j)
        dp[i] += 1
        dp[j] -= 1
        i += 1
    if cnt > 1000000000:
        return -1
    else:
        return cnt


# def findclosest(dp, i):
#     k=1
#     while True:
#         if i-k >=0:
#             if dp[i-k] >1 :
#                 dp[i-k]-=1
#                 break
#         if i+k < len(dp):
#             if dp[i+k] >1:
#                 dp[i+k]-=1
#                 break
# for i in range(1):
#     def intgen(n):
#         for _ in range(n):
#             return [randint(1, n) for _ in range(n)]

#     test = intgen(200000)
#     # print(test)
#     # print(solution([6, 2, 3, 5, 6, 3]))
#     print(solution(test))

print(solution([1, 1, 2]))
