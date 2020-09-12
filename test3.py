def solution(info, query):
    dic = {
        "cpp": 0,
        "java": 1,
        "python": 2,

        'backend': 0,
        'frontend': 1,

        'junior': 0,
        'senior': 1,

        'chicken': 0,
        'pizza': 1
    }

    for i, v in enumerate(query):
        query[i] = query[i].replace(" and ", " ")
    # print(info)
    info_arr = []
    for i, v in enumerate(info):
        info[i] = info[i].split()
    dp = [[[[[] for _ in range(3)] for _ in range(3)]
           for _ in range(3)] for _ in range(4)]
    # print('dp', dp)
    for i, v in enumerate(info):
        # print(dp[dic[v[0]]][dic[v[1]]][dic[v[2]]][dic[v[3]]])
        # print(dic[v[0]], dic[v[1]], dic[v[2]], dic[v[3]])
        # dp[dic[v[0]]][dic[v[1]]][dic[v[2]]][dic[v[3]]] =
        dp[dic[v[0]]][dic[v[1]]][dic[v[2]]][dic[v[3]]].append(int(v[4]))
        # print('v', v)
        dp[3][dic[v[1]]][dic[v[2]]][dic[v[3]]].append(int(v[4]))
        dp[dic[v[0]]][2][dic[v[2]]][dic[v[3]]].append(int(v[4]))
        dp[dic[v[0]]][dic[v[1]]][2][dic[v[3]]].append(int(v[4]))
        dp[dic[v[0]]][dic[v[1]]][dic[v[2]]][2].append(int(v[4]))

        dp[3][2][dic[v[2]]][dic[v[3]]].append(int(v[4]))
        dp[3][dic[v[1]]][2][dic[v[3]]].append(int(v[4]))
        dp[3][dic[v[1]]][dic[v[2]]][2].append(int(v[4]))
        dp[dic[v[0]]][2][2][dic[v[3]]].append(int(v[4]))
        dp[dic[v[0]]][2][dic[v[2]]][2].append(int(v[4]))
        dp[dic[v[0]]][dic[v[1]]][2][2].append(int(v[4]))

        dp[3][2][2][dic[v[3]]].append(int(v[4]))
        dp[3][2][dic[v[2]]][2].append(int(v[4]))
        dp[3][dic[v[1]]][2][2].append(int(v[4]))
        dp[dic[v[0]]][2][2][2].append(int(v[4]))

        dp[3][2][2][2].append(int(v[4]))
    # print(info)
    # print(dp)

    for i, v in enumerate(query):
        query[i] = query[i].split()
        # query[i] = query[i].split()
    # print(query)
    res = []
    # print(query)
    for i, qv in enumerate(query):
        # print('qv', qv)
        count = 0
        first = dic[qv[0]] if qv[0] != '-' else 3
        # if qv[0] != '-':
        #     f = dic[qv[0]]
        # else:
        #     f = 3
        s = dic[qv[1]] if qv[1] != '-' else 2
        # s = dic[qv[1]]
        # t = dic[qv[2]]
        t = dic[qv[2]] if qv[2] != '-' else 2
        # t = dic[qv[2]]
        f = dic[qv[3]] if qv[3] != '-' else 2
        # f = dic[qv[3]]
        # print('fstf', first, s, t, f)
        # if f == '-':
        #     for a in range(3):

        # print('dp fstf', dp[first][s][t][f])
        # print('query value', qv)
        if dp[first][s][t][f]:
            for i, v in enumerate(dp[first][s][t][f]):
                if(v >= int(qv[4])):
                    count += 1
        res.append(count)
    return res

    # count = 0

    # for i, qv in enumerate(query):
    #     for j, iv in enumerate(info):
    #         for idx in range(5):
    #             if idx == 4:
    #                 if int(info[j][idx]) >= int(query[i][idx]):
    #                     # print(qv, iv)
    #                     count += 1
    #             elif query[i][idx] == '-':
    #                 pass
    #             elif info[j][idx] != query[i][idx]:
    #                 break
    #     # print('---')
    #     res.append(count)
    #     count = 0
    # return res


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]	))
