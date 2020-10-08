import sys
n = int(input())
for _ in range(n):
    vis = set()
    a = input()
    b = input()
    for c in a:
        vis.add(c)
    for c in b:
        if c in vis:
            print("YES")
            break
    print("NO")
