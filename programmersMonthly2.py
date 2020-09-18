def solution(n):
    if n == 1:
        return [1]
    arr = [[0 for j in range(i+1)] for i in range(n)]
    i = -1
    j = 0
    cnt = 1
    maxI = n-1
    minI = 0
    visited = set()
    while maxI-minI > 1:
        while i < n-1:
            i += 1
            if (i, j) in visited:
                i -= 1
                break
            visited.add((i, j))
            arr[i][j] = cnt
            cnt += 1
        while j <= n-2:
            j += 1
            if (i, j) in visited:
                j -= 1
                break
            visited.add((i, j))
            arr[i][j] = cnt
            cnt += 1
        while i > 0:
            i -= 1
            j -= 1
            if (i, j) in visited:
                i += 1
                j += 1
                break
            visited.add((i, j))
            arr[i][j] = cnt
            cnt += 1
        maxI -= 1
        minI += 1
    res = []
    for v in arr:
        res += v
    return res

    #     print('1_', i, j)
    #     print('2_', i, j)
    # print('minI', minI)
    #     print('3_', i, j)


    # print('maxI', maxI, 'minI', minI)
print(solution(6))
