def solution(n, lost, reserve):
    dp = [1 for _ in range(n+1)]
    dp[0] = 0
    lost.sort()
    for i, v in enumerate(lost):
        dp[v] = 0
    print(dp)
    reserve.sort()
    for i, v in enumerate(reserve):
        if dp[v] == 0:
            dp[v] = 1
        elif v >= 2 and dp[v-1] == 0:
            dp[v-1] = 1
        elif v+1 <= len(dp)-1 and dp[v+1] == 0:
            dp[v+1] = 1
    print(dp)
    return sum(dp)


print(solution(
    9,
    [3, 7, 8], [2, 6, 8, 9]))
