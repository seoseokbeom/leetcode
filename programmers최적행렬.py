def solution(matrix_sizes):
    res = [matrix_sizes[0][0]]
    for a, b in matrix_sizes:
        res.append(b)
    print(res)
    cnt = 0
    while len(res) >= 3:
        mx, idx = findmax(res[1:-1])
        cnt += multval(res, idx+1)
        res.pop(idx+1)
    return cnt


def multval(arr, i):
    return arr[i-1]*arr[i]*arr[i+1]


def findmax(arr):
    mx, idx = arr[0], 0
    for i, v in enumerate(arr):
        if v > mx:
            mx, idx = v, i
    return [mx, idx]


print(solution([[5, 3], [3, 10], [10, 6], [6, 100]]	))
