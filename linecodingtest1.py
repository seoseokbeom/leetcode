def solution(boxes):
    set1 = set()
    for box in boxes:
        if box[0] in set1:

            set1.remove(box[0])
        else:
            set1.add(box[0])
        if box[1] in set1:
            set1.remove(box[1])
        else:
            set1.add(box[1])

    print(set1)
    return len(set1)//2


print(solution([[1, 2], [2, 3], [3, 1]]		))
