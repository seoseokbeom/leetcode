def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for i, v in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].find(v) == 0:
                return False
    return True
    # return phone_book


print(solution(['119', "1195524432", '88']))
