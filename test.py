def sm():
    global a
    global c
    a = 2
    c = 3


def main():
    global a
    global c
    a = 3
    c = 2
    print(a, c)
    sm()
    print(a, c)


main()
