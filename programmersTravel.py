from collections import defaultdict


def solution(tickets):
    start = defaultdict(lambda: 0)
    end = set()
    for x, y in tickets:
        if x not in start:
            start[x] -= 1
        else:
            start[x] += 1
        if start[x] == 0:
            del start[x]
        if y not in start:
            start[y] += 1
        else:
            start[y] -= 1
        if start[y] == 0:
            del start[y]
        tmp = list(start)
        print(tmp)


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
