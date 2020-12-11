from collections import deque

global mx
mx = 0

cnt = int(input())
queue = deque()
for i in range(cnt):
    queue.appendleft(int(input()))


def dfs(arr, idx, flag, score):
    global mx
    mx = max(mx, score)
    if idx >= len(arr):
        return
    score += arr[idx]
    dfs(arr, idx+2, 0, score)
    if flag == 0:
        dfs(arr, idx+1, 1, score)

dfs(queue,0,0,0)
print(mx)

from collections import deque

cnt = int(input())
queue = deque()
for i in range(cnt):
    queue.appendleft(int(input()))

if len(queue) <= 2:
    print(sum(queue))
else:
    dp = [queue[0], queue[0]+queue[1]]+[0] * (len(queue)-2)
    for i in range(2, len(queue)):
        a = dp[i-2]+queue[i]
        b = 0
        if i > 2:
            b = dp[i-3]+queue[i-1]+queue[i]
        dp[i] = max(a, b)
    print(max(dp[len(queue)-1], dp[len(queue)-2]))

print(queue)
print(dp)


# dfs(queue, 0, 0, 0)
# print(queue)
# print(mx)
