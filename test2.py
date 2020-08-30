
def solution(tar, can):
    ans = []
    can.sort()
    minimum=999
    dfs(can, tar, 0, [], ans)
    for i in range(len(ans)):
        minimum = min(minimum, len(ans[i]))
    return minimum
        
def dfs(num, tar, idx, path, res):
    if(tar==0):
        print(res)
        res.append(path)
        return
    if(tar<0):
        return
    for i in range(idx, len(num)):
        dfs(num, tar-num[i], i, path+[num[i]], res)

def combinationSum2( target, candidates):
    candidates.sort()
    dp = [set() for i in range(target+1)]
    dp[0].add(())
    for num in candidates:
        for t in range(target, 0, -1):
            for prev in dp[t-num]:
                dp[t].add(prev + (num,))
    return list(dp[-1])
def solution(num, cards) :
    cards.sort()
    cards.reverse()
    curr = num
    count=0
    i=0
    while(i<len(cards)):
        if(curr<cards[i]):
            i+=1
            continue
        count += curr//cards[i]
        curr=curr%cards[i]
        print(i,count,  curr)
        if(curr==0): return count 
        i+=1
    return -1


print(solution(8,	[1,4,6]	))