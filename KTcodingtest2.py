
import random
import string

# if S is None or len(S)==0:
#     return []


def solution(S):
    for i in range(len(S)-1):
        for j in range(i+1, len(S)):
            befstr = S[i]
            aftstr = S[j]
            for k in range(len(S[0])):
                if befstr[k] == aftstr[k]:
                    return [i, j, k]
    return []


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("length", length, "is:", result_str)
    return result_str


test = ['aaa', 'bbb', 'cda']
# test = [get_random_string(300) for _ in range(100)]
print(solution(test))
