from collections import defaultdict


def solution(n, costs):
    dic = defaultdict(list)
    for a, b, c in costs:
        dic[(a, b)].append(c)
        dic[(b, a)].append(c)
        vis = set()
        queue = [(0, 0, vis)]
        while queue:
            node = queue.pop(0)
            val = node[0]
            cnt = node[1]
            for key, value in dic.items():
                if key[1] not in node[2] and key[0] == val:
                    viscopy = node[2].copy()
                    viscopy.add(key[1])
                    queue.append((val, cnt+value, viscopy))
        


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]	))
