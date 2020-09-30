# 전공평점구하기
# f1_2 는 1학년 2학기를 의미함
f1_1 = []
f1_2 = [3.5, 4.5]
f2_1 = [3.5, 4.5, 4.5, 4, 4]
f2_2 = [4.5, 4.5, 3.5, 4.5]
f3_1 = [4, 4, 4, 4]
f3_2 = [3, 4.5, 3.5, 4.5, 4.5]
f4_1 = [4.5, 4.5, 4, 4.5, 4, 3.5, 3]
f4_2 = []
test = []
for i in range(1, 5):
    for j in range(1, 3):
        test.extend(eval('f{}_{}'.format(i, j)))

itmajor = [4.5, 4.5, 4.0]
print('IT Major credits I finished in Seoultech:', 9)
print('IT Major credits I finished in CTU:', 11+14)
print('IT Major average GAP in Seoultech :', sum(itmajor)/3)
# print(, , len(test)*3+25)
print('Only Mechanics major credits:', 106 - 34)
print('Mechanics and IT Major Subjects number I finished in Seoultech:', len(test))
print('Mechanics and IT Major Subjects credits I finished in Seoultech:', len(test)*3)
print('Mechanics and IT Major Subjects credits I finished including CVUT:', len(test)*3+25)
print('Mechanics and IT Major Subjects GPA:',  sum(test)/len(test))
# test.extend(f1_1)
# test.extend(f1_2[:])
# # , f1_2, f2_1, f2_2, f3_1, f3_2, f4_1)
# print(test)
