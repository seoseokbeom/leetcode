def solution(arrows):
    if len(arrows) <= 2:
        return 0
    vis = set()
    vis.add((0, 0))
    bef = 0
    curr = 0
    dic = {
        7: (1, -1),
        0: (1, 0),
        1: (1, 1),
        5: (-1, -1),
        4: (-1, 0),
        3: (-1, 1),
        6: (0, -1),
        2: (0, 1)
    }
    history = []
    res = 0
    for i, num in enumerate(arrows):
        a, b = dic[num]
        bfa, bfb = history[i-1] if i > 0 else (0, 0)
        history.append((a+bfa, b+bfb))
        c, d = history[i]
        if (c, d) not in vis:
            vis.add((c, d))
            bef = 0
        else:
            print('visited:', (c, d))
            if i >= 2 and bef == 0 and history[i-2] != history[i]:
                res += 1
                print('res++', history[i])
            bef = 1
    for arr in history:
        print(arr)
    return res


print(solution([2, 6, 2, 6, 6, 0, 3, 7, 2, 4]))
