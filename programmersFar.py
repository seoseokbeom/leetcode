from collections import defaultdict


def solution(n, results):
    dic = defaultdict(list)
    for x, y in results:
        dic[x].append((y, 1))
        dic[y].append((x, -1))
    print(dic)
    for key, val in dic.items():
        for x, y in val:
            arr = dic[x]
            for x2, y2 in arr:
                print(x2, y2)
                if y2 == y:
                    dic[x].append((x2, y2))

    print(dic)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))
