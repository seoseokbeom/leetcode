from collections import deque
from collections import defaultdict


def solution(n, edge):
    routes = defaultdict(list)
    for e1, e2 in edge:
        routes[e1].append(e2)
        routes[e2].append(e1)
    print(routes)
    q = deque([[1, 0]])  # node number, depth
    check = [-1]*(n+1)
    while q:
        index, depth = q.popleft()
        check[index] = depth
        for i in routes[index]:
            if check[i] == -1:
                check[i] = 0
                q.append([i, depth+1])
        depth += 1
    return check.count(max(check))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))
