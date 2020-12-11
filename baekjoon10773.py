stack = []
for _ in range(int(input())):
    node = int(input())
    if node != 0:
        stack.append(node)
    else:
        stack.pop()
print(sum(stack))
