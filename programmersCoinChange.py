import math


def solution(n, coins):
    dp = [0] * (n+1)
    dp[0] = 1
    # for v in coins:
    #     dp[v] = 1
    print(dp)
    for coin in coins:
        for j in range(coin, n+1):
            if j >= coin:
                dp[j] += dp[j-coin]

    print(dp)
    return dp[n]


print(solution(5, [1, 2, 5]))
