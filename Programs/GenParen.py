def genParen(lst, s, l, r):

    if l == 0 and r == 0:
        lst.append(s)
        return

    if r > 0:
        genParen(lst, s+")", l, r-1)
    if l > 0:
        genParen(lst, s+"(", l-1, r+1)


if __name__ == "__main__":
    lst = []
    print("N = 3")
    genParen(lst, "", 3, 0)
    print(lst)

    # print("N = 2")
    # genParen(lst,"",2,0)
    # print(lst)

    # print("N = 4")
    # genParen(lst,"",4,0)
    # print(lst)
