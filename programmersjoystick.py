def solution(name):
    updowncnt = 0
    for c in name:
        cnt1 = min(ord(c)-64-1, ord('Z')-ord(c)+1)
        updowncnt += cnt1
    # name = ''.join(list(name)[1:])
    rl_cnt = len(name)-1
    # print(rl_cnt)
    cnt2 = 0
    for i in range(len(name)-1, -1, -1):
        if name[i] == 'A':
            cnt2 += 1
        else:
            rl_cnt -= cnt2
            break
    for i in range(1, len(name)):
        if name[i] != 'A':
            rl_cnt = min(rl_cnt, len(name)-i)
            break
    print(rl_cnt)
    i, j = 0, len(name)-1
    diffleft, diffright = 0, len(name)
    while i <= j:
        if i == j:
            if name[i] == 'A':
                break
            else:
                if diffleft >= len(name)-diffright:
                    diffleft = i
                else:
                    diffright = i
                break
        if name[i] != 'A':
            diffleft = i
        if name[j] != 'A':
            diffright = j
        i += 1
        j -= 1
    # print('dif:', diffleft, len(name)-diffright)
    rl_cnt = min(rl_cnt, diffleft*2+len(name)-diffright,
                 diffleft+2*(len(name)-diffright))
    print(updowncnt, rl_cnt)
    return updowncnt+rl_cnt


# print(solution("BAABA"))
# print(solution("ABABA"))
print(solution("BBAABAABB"))
# print(solution("BBABAAAB"))


def solution(n, arr1, arr2):
    res = []
    for de1, de2 in zip(arr1, arr2):
    b = str(bin(de1 | de2))[2:]
    b = '0' * (n - len(b)) + b
    b = b.replace('1', '#')
    b = b.replace('0', ' ')
    res.append(b)
    return res
