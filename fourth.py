def divienders(numb):
    numbers = [0] * numb
    inte = 0
    for i in range(numb):
        if numb % (i + 1) == 0:
            numbers[inte] += i + 1
            inte += 1
    if sum(numbers) / 2 == numb:
        return True

    return False


print(divienders(int(input())))
