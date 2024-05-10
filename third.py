test_numb = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
}
test_lo = {
    "q",
    "w",
    "e",
    "r",
    "t",
    "y",
    "u",
    "i",
    "p",
    "o",
    "a",
    "s",
    "d",
    "f",
    "g",
    "h",
    "j",
    "k",
    "l",
    "z",
    "x",
    "c",
    "v",
    "b",
    "n",
    "m",
}
test_ss = {
    "@",
    "#",
    "$",
}
test_up = {
    "Q",
    "W",
    "E",
    "R",
    "T",
    "Y",
    "U",
    "I",
    "O",
    "P",
    "A",
    "S",
    "D",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "Z",
    "X",
    "C",
    "V",
    "B",
    "N",
    "M",
}
while True:
    pasword = str(input())

    if len(pasword) < 8:
        print("invalid")
        continue
    elif len(pasword) > 12:
        print("invalid")
        continue
    pasword = set(pasword)
    if test_lo.isdisjoint(pasword):
        print("invalid")
        continue
    elif test_numb.isdisjoint(pasword):
        print("invalid")
        continue
    elif test_ss.isdisjoint(pasword):
        print("invalid")
        continue
    elif test_up.isdisjoint(pasword):
        print("invalid")
        continue
    else:
        print("valid")
        break
