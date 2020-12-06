import sys


tmp = [1, 2, 3]+[0]*999999
# print(len(tmp))
# for i in range(3, 900000):
#     tmp[i] = tmp[i-1]+tmp[i-2]

# print(tmp[0:100])
print(sys.getsizeof(tmp))
