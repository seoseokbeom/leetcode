def solution(answers):
    dic3 = {
        0: 3,
        1: 1,
        2: 2,
        3: 4,
        4: 5
    }
    dic2 = {
        0: 1,
        1: 3,
        2: 4,
        3: 5
    }
    cnt1 = cnt2 = cnt3 = 0
    for i, v in enumerate(answers):
        if i % 5+1 == v:
            cnt1 += 1
        if i % 2 == 0 and v == 2:
            cnt2 += 1
        elif i % 2 == 1:
            tmp = (i//2) % 4
            if v == dic2[tmp]:
                print(v)
                cnt2 += 1
        tmp2 = (i % 10)//2
        if dic3[tmp2] == v:
            cnt3 += 1
    mx = max(cnt1, cnt2, cnt3)
    return [i+1 for i, v in enumerate([cnt1, cnt2, cnt3]) if v == mx]
    # resarr = [(v, i+1) for i, v in enumerate([cnt1, cnt2, cnt3])]
    # return resarr


print(solution([1, 1, 1, 1, 1]	))
