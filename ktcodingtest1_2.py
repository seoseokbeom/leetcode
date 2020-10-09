def solution(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    if n <= 2:
        return dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n] % 1000000007


# for i in range(1, 300):
print(solution(60000))
