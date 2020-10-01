def solution(A, B):
    res = 0
    for i, v in enumerate(A):
        res += v*B[(i+1) % len(B)]
        print(res)
    return res


print(solution([1, 4, 2],	[5, 4, 4]))
