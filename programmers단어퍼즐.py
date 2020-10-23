def solution(strs, t):
    strs.sort(key=lambda x: len(x), reverse=True)
    queue = []
    for v in strs:
        idx = t.find(v)
        if idx != -1:
            s = t[:idx]+t[idx+len(v):]
            print(s, v)
            queue.append(s)
    cnt = 1
    while queue:
        for remain in queue:
            remainnode =
            for v in strs:
                idx = remain.find(v)
                if idx != -1:
                    s = remain[:idx]+remain[idx+len(v)]

        for v in strs:
            idx = t.find(v)
            if idx != -1:
                s = t[:idx]+t[idx+len(v):]
                print(s, v)
                queue.append(s)

    return queue

    print(t.find('apps'))
    return t.find('apps')


print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
