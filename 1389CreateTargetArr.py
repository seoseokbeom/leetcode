
def createTargetArray(nums, index):
    res = []
    for i, v in enumerate(nums):
        res = res[:index[i]]+[v]+res[index[i]:]
    return res


print(createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]
                        ))
