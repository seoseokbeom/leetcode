from collections import Counter

a = 'abcdaad'
print(Counter(a))
print(Counter(a).most_common(1))
print(Counter(a).most_common(1)[0])
print(Counter(a).most_common(1)[0][0])
print([Counter(a).most_common(1)][0][0])
print(list(Counter(a).most_common(1))[0])
