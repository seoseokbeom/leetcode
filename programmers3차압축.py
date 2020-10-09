from collections import defaultdict
from random import randint


def solution(msg):
    msg = msg+'_'
    dic = defaultdict(lambda: None)
    res = []
    for i in range(ord('A'), ord('Z')+1):
        dic[chr(i)] = i-64
    endidx = 0
    i = 0
    # for i in range(len(msg)):
    while i < len(msg)-1:
        endidx = i
        while endidx < len(msg)-1 and dic[msg[i:endidx+1]]:
            endidx += 1
        res.append(dic[msg[i:endidx]])
        dic[msg[i:endidx+1]] = len(dic)
        print(i, endidx, res,  msg[i:endidx+1], len(dic))
        if endidx == len(msg)-1:
            break
        i = endidx
    # print('last:', dic[msg[i:]])
    # res.append(dic[msg[i:]])
    print(dic)
    return res
    if endidx == len(msg):
        res.append(dic[msg[i:endidx]])
        return res


# test = 'ABC'
# test2 = ''
# for i in range(10):
#     test2 += test[randint(0, 1)]

# print(test2)
# print(solution(test2))
# print(solution('D'))
print(solution('KAKAO'))

# print(solution('KAKAOKAKAOKAKAOKAKAO'))
# print(solution('K A KA O KA KAO KAK A OK AK AO'))
# print(solution('A AA AAA AAAA AAAAA AAAAAA'))
