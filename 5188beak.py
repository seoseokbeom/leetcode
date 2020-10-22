
# T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# global res

# res = float('inf')


def dfs(arr, i, j, cnt):
    if i == j == len(arr)-1:
        global res
        res = min(res, cnt)
        return
    if i+1 < len(arr):
        dfs(arr, i+1, j, cnt+arr[i+1][j])
    if j+1 < len(arr):
        dfs(arr, i, j+1, cnt+arr[i][j+1])


# print(dfs([[2, 4, 1, 3], [1, 1, 7, 1], [9, 1, 7, 10], [5, 7, 2, 4]], 0, 0, 2))
# print(res)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')
    dfs(arr, 0, 0, arr[0][0])
    print('#{} {}'.format(test_case, res))
