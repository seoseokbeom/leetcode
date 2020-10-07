import math


def solution(matrix_sizes):
    table = [[math.inf for _ in range(len(matrix_sizes))]
             for _ in range(len(matrix_sizes))]
    print(table)
    for idx in range(len(matrix_sizes)):
        table[idx][idx] = 0

    for gap in range(1, len(matrix_sizes)):
        for start in range(len(matrix_sizes)):
            end = start + gap
            if end >= len(matrix_sizes):
                break
            for sep in range(start, end):
                table[start][end] = min(
                    table[start][end],
                    table[start][sep] + table[sep+1][end] +
                    (matrix_sizes[start][0] * matrix_sizes[sep]
                     [1] * matrix_sizes[end][1])
                )
    for v in table:
        print(v)
    return table[0][-1]


# def solution(matrix_sizes):
#     res = [matrix_sizes[0][0]]
#     for a, b in matrix_sizes:
#         res.append(b)
#     print(res)
#     cnt = 0
#     while len(res) >= 3:
#         mx, idx = findmax(res[1:-1])
#         cnt += multval(res, idx+1)
#         res.pop(idx+1)
#     return cnt


# def multval(arr, i):
#     return arr[i-1]*arr[i]*arr[i+1]


# def findmax(arr):
#     mx, idx = arr[0], 0
#     for i, v in enumerate(arr):
#         if v > mx:
#             mx, idx = v, i
#     return [mx, idx]


# print(solution([[5, 3], [3, 10], [10, 6]]	))
print(solution([[5, 3], [3, 10], [10, 6], [6, 100]]	))
