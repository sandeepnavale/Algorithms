def genParen(s, l, r):
    if l == 0 and r == 0:
        print(s)
        return

    if l > 0: genParen(s + "(", l - 1, r + 1)
    if r > 0: genParen(s + ")", l, r - 1)


if __name__ == "__main__":
    # print("N = 2")
    # genParen("", 2, 0)

    # print("N = 3")
    # genParen("", 3, 0)
    #
    print("N = 4")
    genParen("", 4, 0)
    #
