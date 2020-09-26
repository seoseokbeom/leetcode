def solution(n, words):
    fir = sec = -1
    idx = -1
    vis = set()
    vis.add(words[0])
    for i in range(1, len(words)):
        if words[i] in vis or words[i][0] != words[i-1][-1]:
            idx = i
            break
        vis.add(words[i])
    print(idx)
    if idx == -1:
        return [0, 0]
    fir = idx % n+1
    sec = idx//n+1
    return [fir, sec]


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]	))
