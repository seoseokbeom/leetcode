a = int(input())
b, c, d = 1, 2, 3
for i in range(3, a):
    b, c = c, d
    d = (b+c) % 15746
print(d) if a > 2 else print(a)
