def solution(ball, order):
    res = []
    tmp = []
    for i, o in enumerate(order):
        while len(tmp) != 0 and (ball[-1] in tmp or ball[0] in tmp):
            for j, tmp_ball in enumerate(tmp):
                if tmp_ball == ball[-1]:
                    res.append(tmp[j])
                    tmp.pop(j)
                    ball.pop(-1)
                    break
                elif tmp_ball == ball[0]:
                    res.append(tmp[j])
                    tmp.pop(j)
                    ball.pop(0)
                    break

        if ball[-1] == o or ball[0] == o:
            res.append(o)
            if ball[-1] == o:
                ball.pop(-1)
            elif ball[0] == o:
                ball.pop(0)
        else:
            tmp.append(o)

    while len(tmp) != 0 and (ball[-1] == tmp[0] or ball[0] == tmp[0]):
        res.append(tmp[0])
        if ball[-1] == tmp[0]:
            ball.pop(-1)
        else:
            ball.pop(0)
        tmp.pop(0)
    return res


print(solution([41, 21, 13, 42, 15, 26, 15, 19, 24]		,
               [21, 26, 42, 13, 15, 41, 24, 21, 19]		))
