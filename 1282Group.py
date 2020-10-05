from collections import defaultdict


def groupThePeople(groupSizes):
    count = defaultdict(list)
    for i, size in enumerate(groupSizes):
        count[size].append(i)
    print(count.items())
    for s, l in count.items():
        for i in range(0, len(l), s):
            print(l[i:i + s])

    return [l[i:i + s] for s, l in count.items() for i in range(0, len(l), s)]

# def groupThePeople(groupSizes):
#     for i in range(len(groupSizes)):
#         groupSizes[i] = (groupSizes[i], i)
#     groupSizes.sort(key=lambda x: x[0])
#     res = []
#     i = 0
#     print(groupSizes)
#     while i < len(groupSizes):
#         res.append([groupSizes[j][1] for j in range(i, groupSizes[i][0]+i)])
#         i += groupSizes[i][0]
#         print(res, i)

#     return res


print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))
