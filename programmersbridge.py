def solution(bridge_length, weight, truck_weights):
    dp = [0] * (bridge_length*len(truck_weights)+10)
    i = 1
    l = 0
    for k, tw in enumerate(truck_weights):
        if dp[i]+tw > weight:
            i = bridge_length+i-1
        for j in range(i, bridge_length+i):
            dp[j] += tw
        i += 1
        print(dp)
    dp[0] = 1
    return dp.index(0)


# a=solution()
print(solution(	3, 10, [7]))
