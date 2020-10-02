def solution(name):
    res = 0
    for c in name:
        cnt1 = min(ord(c)-64, ord('Z')-ord(c))
        res += cnt1
    return res


print(solution("JEROEN"))
