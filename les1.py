line1 = input("введите строку 1: ") + "\n"
line2 = input("введите строку 2: ") + "\n"
line3 = input("введите строку 3: ") + "\n"
line4 = input("введите строку 4: ") + "\n"
list_line = [line1, line2, line3, line4]
with open("test12.txt", "w") as f:
    for index, item in enumerate(list_line):
        if index <= 1:
            f.write(item)
with open("test12.txt", "a") as f:
    for index, item in enumerate(list_line):
        if index > 1:
            f.write(item)















