
from collections import defaultdict


def solution(n, results):
    dic = defaultdict(list)
    for x, y in results:
        dic[x].append((y, 1))
        dic[y].append((x, -1))
    for key, val in dic.items():
        for x, y in val:
            arr = dic[x]
            for x2, y2 in arr:
                if y2 == y:
                    if (x2, y2) not in dic[key]:
                        dic[key].append((x2, y2))
    cnt = 0
    for key, val in dic.items():
        if len(val) == n-1:
            cnt += 1
    return cnt


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	))
