from collections import defaultdict


def solution(tickets):
    tickets.sort(key=lambda x: x[1], reverse=True)
    res = ['ICN']
    start = 'ICN'
    dic = defaultdict(list)
    for v in tickets:
        dic[v[0]].append(v[1])
    cnt = len(tickets)
    while cnt:
        end = dic[start].pop()
        if len(dic[end]) == 0 and len(res) < len(tickets):
            dic[start].insert(0, end)
            continue
        res.append(end)
        start = end
        cnt -= 1
    return res


print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ['B', "A"]]))
