def solution(routes):
    mn = mx = routes[0][0]
    for arr in routes:
        mn = min(mn, min(arr))
        mx = max(mx, max(arr))
    dp = [0 for _ in range(mx-mn+1)]

    for arr in routes:
        for i in range(arr[0], arr[1]+1):
            # print(i)
            if i == arr[0] or i == arr[1]:
                dp[i-mn] += 0.99
            else:
                dp[i-mn] += 1
    cnt = 0
    a = b = c = '#'
    print(dp)
    cnt2 = 0
    for i in range(0, len(dp)):
        if dp[i] != c:
            a, b, c = b, c, dp[i]
        if a != '#' and b != '#' and c != '#' and a < b and b > c:
            cnt += 1
            a, b, c = '#', '#', dp[i]
    if dp[-2] < dp[-1]:
        cnt += 1
    return cnt


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]	))
