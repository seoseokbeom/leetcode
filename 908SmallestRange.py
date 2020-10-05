def smallestRangeI(A, K):
    sm = min(A)
    mx = max(A)
    mid = (sm+mx)//2
    sm = sm+min(mid-sm, K)
    mx = mx-min(mx-mid, K)
    return mx-sm


print(smallestRangeI(A=[0, 11], K=2))
