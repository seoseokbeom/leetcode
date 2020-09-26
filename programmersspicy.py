def solution(s, K):
    cnt = 0
    while len(s) >= 2:
        s.sort()
        print(s)
        if s[0] < K:
            s[1] = s[0]+(s[1])*2
            s.pop(0)
            cnt += 1
        elif s[0] >= K:
            break
    if len(s) == 1 or s[0] < K:
        return -1
    return cnt


# print(solution([1, 2, 3, 9, 10, 12],	7))
print(solution([12, 1, 2, 1, 1, 3, 9, 10], 2))
