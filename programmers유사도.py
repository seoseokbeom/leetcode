import re
from collections import defaultdict


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    set1 = defaultdict(int)
    set2 = defaultdict(int)
    regex = re.compile('[@_!#$%^&*+()<>?/\|}{~:0-9]')
    for i in range(1, len(str1)):
        a = str1[i-1:i+1]
        if regex.search(a) == None:
            set1[str1[i-1:i+1]] += 1
    for j in range(1, len(str2)):
        a = str2[j-1:j+1]
        if regex.search(a) == None:
            set2[a] += 1
    res = 0
    # res &= set1
    print(set1, set2)
    # print(set1, set2)
    # print(set1 & set2)
    # print(set1 | set2)
    # print(len(set1 & set2) / len(set1 | set2))
    # print(int(len(set1 & set2) / (len(set1) + len(set2)) * 65536))
    # return 65536 if len(set1 | set2) == 0 else (int(len(set1 & set2) / len(set1 | set2) * 65536))


print(solution(	"aa1+aa2", "AAAA12"))
