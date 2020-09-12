def solution(play_time, adv_time, logs):
    # 2d arr.
    arr = []
    for i, log in enumerate(logs):
        # logs[i] = ':'. join(logs[i].replace()
        logs[i] = logs[i].replace(':', ' ')
        logs[i] = logs[i].split('-')
    s_arr = []
    for i, log in enumerate(logs):
        tmp = []
        for j, time in enumerate(log):
            log[j] = log[j].split()
            s = 0
            for k, hms in enumerate(log[j]):
                if k == 0:
                    s += int(hms) * (60**2)
                elif k == 1:
                    s += int(hms) * 60
                elif k == 2:
                    s += int(hms)
            tmp.append(s)
        s_arr.append(tmp)
    print(s_arr)

    acc_arr = []
    for i, sec in enumerate(s_arr):
        print('---')
        if len(acc_arr) == 0:
            acc_arr.append([sec[0], 1])
            acc_arr.append([sec[1], 1])
            pass
        for j, s_arr in enumerate(acc_arr):
            if(s_arr > sec):
                pass
            else:

                # print(acc_arr)

    return arr


print(solution("02:03:55"	, "00:14:15"	, [
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	))
