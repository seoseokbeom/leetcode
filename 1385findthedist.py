def findTheDistanceValue(A, B, d):
    return sum(all(abs(a-b) > d for b in B) for a in A)


print(findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
