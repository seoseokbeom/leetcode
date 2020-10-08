from collections import deque


def solution(land, height):
    arr = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    cnt = 1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if arr[i][j] == 0:
                dfs(land, i, j, arr, cnt, height)
                cnt += 1

    # for i in range(len(land)):
    #     for j in range(len(land[0])):

    return arr


def dfs(land, i, j, arr, cnt,  height):
    arr[i][j] = cnt
    for a, b in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if a >= 0 and a < len(land) and b >= 0 and b < len(land[0]) and arr[a][b] == 0:
            if abs(land[i][j]-land[a][b]) <= height:
                dfs(land, a, b, arr, cnt,  height)


print(solution([[10, 11, 10, 11], [2, 21, 20, 10],
                [1, 20, 21, 11], [2, 1, 2, 1]], 1	))


print((1, 2)+(5, 1))
