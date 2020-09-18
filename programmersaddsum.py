import itertools


def solution(numbers):
    arriter = itertools.combinations(numbers, 2)
    res = set()
    for v in arriter:
        res.add(sum(v))
    return sorted(list(res))


print(solution([5, 0, 2, 7]))
