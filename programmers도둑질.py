def solution(money):
    # if len(money) < 3:
    #     return max(money) if len(money) != 0 else 0
    dp = [0]*(len(money))
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    dp2 = [0]*(len(money))
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    print(dp)
    for i in range(3, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    print(dp2)
    return max(dp[len(money)-2], dp2[len(money)-1])


print(solution([100, 55, 12, 55, 1100]))
