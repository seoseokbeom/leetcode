def solution(land):
    vis = set()
    cnt = 0
    vis = -1
    for i in range(1, len(land)):

        for j in range(len(land[0])):
            mxval = float('-inf')
            for k in range(len(land[0])):
                if k == j:
                    continue
                mxval = max(mxval, land[i-1][k])
            land[i][j] += mxval
    return max(land[-1])

    # for i, row in enumerate(land):
    #     ml = (float('-inf'), 0)
    #     sl = (float('-inf'), 0)
    #     for j, v in enumerate(row):
    #         if v > ml[0]:
    #             sl = ml
    #             ml = (v, j)
    #         elif ml[0] > v > sl[0]:
    #             sl = (v, j)
    #     print(sl, ml)
    #     if vis != ml[1]:
    #         cnt += ml[0]
    #         vis = ml[1]
    #     else:
    #         cnt += sl[0]
    #         vis = sl[1]


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]		))
