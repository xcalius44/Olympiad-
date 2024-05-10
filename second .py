nambers = [0] * 9


def colculation():
    number = str(input())
    if len(number) > 100000:
        print("to many nambers")
    else:
        for n in number:
            n = int(n) - 1
            nambers[n] += 1

    print(nambers)


colculation()
