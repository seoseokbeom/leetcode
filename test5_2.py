def solution(play_time, adv_time, logs):
    # 2d arr.
    arr = []
    n_playtime = play_time.replace(':', ' ')
    n_playtime = n_playtime.split()
    s = 0
    for k, hms in enumerate(n_playtime):
        if k == 0:
            s += int(hms) * (60**2)
        elif k == 1:
            s += int(hms) * 60
        elif k == 2:
            s += int(hms)
    n_playtime = s
    # print('n_playtime', n_playtime)

    n_advtime = adv_time.replace(':', ' ')
    n_advtime = n_advtime.split()
    s = 0
    for k, hms in enumerate(n_advtime):
        if k == 0:
            s += int(hms) * (60**2)
        elif k == 1:
            s += int(hms) * 60
        elif k == 2:
            s += int(hms)
    n_advtime = s
    # print('n_advtime', n_advtime)
    if(n_playtime == n_advtime):
        return '00:00:00'

    s = 0
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
    # print('s_arr', s_arr)
    # acc_arr = [[s_arr[0][0], 1], [s_arr[0][1], 1]]
    # print('acc_arr', acc_arr)
    idx = 0
    acc_arr = []
    # make arr dynamically
    track = [0 for _ in range(60*60*100)]
    for i in range(len(s_arr)):
        track[s_arr[i][0]] = 1
        track[s_arr[i][1]] = -1
        # s_arr[i][1] = 20
    for i in range(1, len(track)):
        track[i] += track[i-1]

    # print(track)
    tmp_acc_time = 0
    x_position = 60*60*100-n_advtime
    for i in range(60*60*100-1, 60*60*100-1-n_advtime, -1):
        tmp_acc_time += track[i]
    # print('tmp_acc_time', tmp_acc_time)
    tmpv = 0
    # print(track)
    maxv = tmp_acc_time
    x_position = 60*60*100-n_advtime
    for j in range(60*60*100-1-n_advtime, -1, -1):
        tmp_acc_time = tmp_acc_time + track[j] - (track[j+n_advtime])
        if(tmp_acc_time >= maxv):
            x_position = j
            maxv = tmp_acc_time
        # print(tmpv, j)
    # print(tmp_acc_time, '초')
    # print(tmp_acc_time//60//60, '시')
    # print((tmp_acc_time//60) % 60, '분')
    # print('position')
    # print(x_position, '초')
    # print(x_position//60//60, '시')
    # print((x_position//60) % 60, '분')
    # print((x_position % 60) % 60, '초')
    h = str(x_position//60//60)
    if h == '0':
        a = '00'
    elif len(h) == 1:
        a = '0'+h
    else:
        a = h
    m = str((x_position//60) % 60)
    if m == '0':
        b = '00'
    elif len(m) == 1:
        b = '0'+m
    else:
        b = m
    s = str((x_position % 60) % 60)
    if s == '0':
        c = '00'
    elif len(s) == 1:
        c = '0'+s
    else:
        c = s
    # a = str(x_position//60//60)
    # b = str((x_position//60) % 60)
    # c = str((x_position % 60) % 60)

    result = ''
    result += a
    result += ':'
    result += b
    result += ':'
    result += c
    return result


print(solution("02:03:55"	, "00:14:15"	, [
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	))
print(solution("99:59:59"		, "25:00:00"		, [
      "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]		))
print(solution("50:00:00"		, "50:00:00"		, [
      "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]		))

# track[i] = -1
# s_arr[i][1] = 20

# for i, secv in enumerate(s_arr):
#     first = secv[0]
#     second = secv[1]
#     for j, accv in enumerate(acc_arr):
#         if(accv < first):
#             pass
#         elif(acc == first):
#             acc_arr[j][1] += 1
#             idx = j
#             break
#         else:
#             acc_arr.insert(j, [first, 1])
#             idx = j
#             break
#     for k in range(j+1, len(acc_arr)):
#         if second < acc_arr[k]:
#             acc_arr.insert(k, [second, acc_arr[k]+1])

# for(var i=1
#     i < s_arr.length
#     i++) {
#     for(var j=0
#         j < acc_arr.length
#         j++) {

#     }
# # }
# print(acc_arr)
