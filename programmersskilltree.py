def solution(skill, skill_trees):
    res = []
    tmp = []
    cnt = 0
    for i, v in enumerate(skill_trees):
        tmp = []
        for j, v2 in enumerate(skill):
            a = v.find(v2)
            tmp.append(a) if a != -1 else tmp.append(float('inf'))
        print(tmp)
        for i in range(1, len(tmp)):
            print(i, len(tmp)-1)
            if tmp[i] < tmp[i-1]:
                break
            if i == len(tmp)-1:
                cnt += 1
    return cnt


a = 'bacde'
solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
