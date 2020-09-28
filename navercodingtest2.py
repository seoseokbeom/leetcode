def solution(blocks):
    row = len(blocks)
    dp = [[0 for _ in range(row)] for _ in range(row)]
    for i, arr in enumerate(blocks):
        j, v = arr
        # print(j, v)
        dp[i][j] = v

    for i, arr in enumerate(blocks):
        if i == 0:
            continue
        j, v = arr
        l = j
        while l >= 1:
            l -= 1
            # print('l:', i, l)
            # print(dp[i-1][l], dp[i][l])
            dp[i][l] = dp[i-1][l]-dp[i][l+1]
        r = j
        while r <= i-1:
            r += 1
            # print('r:', i, r)
            # print(i, r)
            dp[i][r] = -dp[i][r-1]+dp[i-1][r-1]
    for r in dp:
        print(r)
    res = []
    for i in range(row):
        for j in range(i+1):
            res.append(dp[i][j])
    return res

    # return dp


# print(solution([[0, 92], [0, 22]]))
# print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))
print(solution([[0, 50], [0, -55], [2, 90],
                [1, 94], [4, -13], [4, -14], [4, -15]]))
