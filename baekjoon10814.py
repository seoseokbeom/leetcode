arr = [[] for _ in range(200)]

for i in range(int(input())):
    a, b = input().split()
    arr[int(a)].append(b)

for i in range(2, 200):
    for v in arr[i]:
        print(i, v)
