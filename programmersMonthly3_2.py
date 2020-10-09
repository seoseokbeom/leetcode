from collections import defaultdict


def solution(n, edges):
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dic = defaultdict(list)
    for a, b in edges:
        dic[a].append(b)
        dic[b].append(a)
        arr[a][b] = arr[b][a] = 1
    # print(dic)
    for a, b in edges:
        vis = set()
        vis.add(a)
        vis.add(b)
        rec(a, b, arr, vis, dic, 2)
        rec(b, a, arr, vis, dic, 2)
    # for row in arr:
    #     print(row)
    mx = float('-inf')
    for i in range(1, len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                tmp = sorted([arr[j][i], arr[k][i], arr[k][j]])
                mx = max(mx, tmp[1])
    return mx

    # newarr = []
    # for i, row in enumerate(arr):
    #     newarr.extend(row[1:i])
    # newarr.sort(reverse=True)
    # return newarr[1]

    # f, s, t = float('-inf'), float('-inf'), float('-inf')
    # for i in range(1, len(arr)):
    #     for j in range(1, i):
    #         if arr[i][j] >

    for row in arr:
        print(row)

    return arr


def rec(num, newnum, arr, vis, dic, cnt):
    elemlist = dic[newnum]
    for e in elemlist:
        if e not in vis:
            arr[num][e] = cnt
            arr[e][num] = cnt
            vis.add(e)
            rec(num, e, arr, vis, dic, cnt+1)


print(solution(5, [[1, 2], [2, 3], [3, 4], [3, 5]]	))
# print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]	))
