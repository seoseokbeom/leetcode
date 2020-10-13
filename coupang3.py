
from collections import defaultdict


def solution(k, score):
    dic1 = defaultdict(int)
    dic2 = defaultdict(set)
    for i, v in enumerate(score):
        if i == len(score)-1:
            break
        dic1[v-score[i+1]] += 1
        dic2[v-score[i+1]].add(i+1)
        dic2[v-score[i+1]].add(i+2)
    res = len(score)
    print(dic2)
    for key, val in dic1.items():
        print(key, val)
        if val >= k:
            res -= len(dic2[key])
    return res


print(solution(3, [24, 22, 20, 10, 5, 3, 2, 1]))
