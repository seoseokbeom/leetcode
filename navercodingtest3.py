from collections import defaultdict


def solution(n, edges):
    dic = defaultdict(list)
    for parent, child in edges:
        dic[parent].append(child)
    node = 0
    print(dic)
    res = float('inf')
    n = 0
    cnt = 0
    tmp = []
    while len(dic[n]) != 0:
        nodearr = dic[n]
        cnt += len(dic[n])-1
        print(n)
        for i in range(1, len(dic[n])):
            tmp.append(nodearr[i])
            n = tmp.pop(0)
    return cnt

    # queue = [[(1, 2)], [(2, 2)]]
    # while queue:
    #     length = len(queue)
    #     tmp = []
    #     allsubnodes = []
    #     for k in range(length):
    #         print(queue)
    #         node = queue.pop(0)
    #         cnt = 0
    #         for i in range(length):
    #             if i == k:
    #                 continue
    #             cnt += 1
    #             for v in dic[node[0]]:
    #                 tmp.append((v, cnt+node[1]))
    #             allsubnodes.append(tmp)
    #         # allsubnodes.append((dic[node[0]], cnt+node[1]))
    #         # allsubnodes.append(dic[node[0]])
    #     # allsubnodes.append(tmp)
    #     print(allsubnodes)
    #     for v in tmp:
    #         print('cnt', cnt, node[1])
    #         queue.append((v, cnt+node[1]))
    # # return dic


# def recur(dic):
print(solution(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9],
                    [3, 10], [4, 11], [4, 12], [4, 13]]))
