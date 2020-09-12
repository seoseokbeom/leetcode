def solution(orders, course):
    res = []
    # 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
    for i, v in enumerate(orders):
        orders[i] = ''.join(sorted(orders[i]))
    print(orders)
    tmp = []
    print(makeset("ABCDE", [], 0, 2))
    print(tmp)
    return res


def makeset(order, arr, i, count):
    if(count == 0):
        tmp.append(arr)
        return
    elif i >= len(order):
        return
    arr.append(order[i])
    makeset(order, arr, i+1, count-1)
    arr.pop()


# self.tmp = []
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	, [2, 3, 4]	))
