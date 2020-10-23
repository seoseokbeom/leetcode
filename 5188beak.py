def dfs(arr, i, j, cnt):
    if i == j == len(arr)-1:
        global res
        res = min(res, cnt)
        return
    if i+1 < len(arr):
        dfs(arr, i+1, j, cnt+arr[i+1][j])
    if j+1 < len(arr):
        dfs(arr, i, j+1, cnt+arr[i][j+1])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')
    dfs(arr, 0, 0, arr[0][0])
    print('#{} {}'.format(test_case, res))
