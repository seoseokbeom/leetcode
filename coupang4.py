
from collections import defaultdict
from collections import deque


def solution(depar, hub, dest, roads):
    print('roads', len(roads))
    dic = defaultdict(list)
    res = 0
    for start, end in roads:
        dic[start].append(end)
    queue = deque()
    for v in dic[depar]:
        queue.append((v, 0))
    # print(queue)
    while len(queue):
        for i in range(len(queue)):
            node, visited = queue.popleft()
            # print(node, visited)
            if(node == dest):
                if(visited):
                    res += 1
            elif(node == hub):
                for v in dic[node]:
                    queue.append((v, 1))
            else:
                for v in dic[node]:
                    queue.append((v, visited))
    return res % 10007


print(solution(1, 5, 13, [[1, 4], [1, 2], [12, 13], [5, 6], [5, 9], [4, 5], [2, 5], [5, 8],
                          [8, 11], [11, 12], [2, 6], [2, 3], [3, 7], [6, 7], [7, 9], [9, 12], [9, 10], [10, 13]]))
# print(solution('s', 'dg', 'y',
#                [['u', 'b'], ['dj', 'u'], ['dj', 'g'], ['s', 'dj'], ['s', 'u'], ['dj', 'dg'], ['g', 'b'],
#                    ['dg', 'g'], ['dg', 'b'], ['u', 'dg'], ['g', 'y'], ['b', 'y']
#                 ]))
