# str S return Max count a

# a = 'aabaabb'
# print(a.replace('a', ''))

import random
import string


def solution(S):
    cnt = 0
    for v in S:
        if v == 'a':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return -1

    newS = S.replace('a', '')
    return 3*len(newS)+2 - len(S)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice('abcde') for i in range(length))
    # result_str = ''.join(random.choice(letters) for i in range(length))
    print("length", length, "is:", result_str)
    return result_str


# test = [get_random_string(300) for _ in range(100)]
for i in range(10):
    test = get_random_string(200)
    print(solution(test))
# print(solution('abaaa'))
# print(solution('baaa'))
# print(solution('bb'))
# print(solution('bbc'))
# print(solution('bbac'))
# print(solution('baaaa'))
# print(solution('abaa'))
# print(solution('aabaa'))
# print(solution('aabaacaa'))
# print(solution('aabaacaaa'))
