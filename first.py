n = ""
line = list(str(input()))
line[0] = line[0].upper()
for i in range(len(line)):
    if line[i - 1] == "_":
        line[i] = line[i].upper()
for i in line:
    n = n + i
print(n)
