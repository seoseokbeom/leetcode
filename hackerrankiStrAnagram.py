
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    set1 = set(list(a))
    set2 = set(list(b))
    return (len(a)+len(b) - 2*len(set1.intersection(set2)))


print(makeAnagram('cde', 'abc'))
