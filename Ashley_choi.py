level = int(1)
rows = int(input("Enter number"))
print(level)
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print("\n")

level = 1 + level
print(level)
for i in range(1, rows + 1):
    space = " " * (rows - i)
    star = "*" * (i + (i - 1))
    print(space, star)

level = 1 + level
print(level)
for i in range(1, rows + 1):
    space = " " * (rows - i)
    star = "*" * (2 * i)
    print(space, star)

level = 1 + level
print(level)
for i in range(1, rows + 1):
    space = " " * (rows - i)
    star = "*" * (2*i - 1)
    print(space, star)
for j in range(1, rows + 1):
    space = " " * (j)
    star = "*" * (rows - j + (rows - j - 1))
    print(space, star)

level = 1 + level
print(level)
star = 0
list1=[]
for i in range(1, rows + 1):
    if i > 1:
        star = 2
    elif i == 1:
        star = 1
    space = " " * (rows - i)
    list1.append(rows-i)
    space2 = " " * (((2 * rows) - 1) - (2 * (rows - i) + star))
    list1.append(((2 * rows) - 1) - (2 * (rows - i) + star))
    if star > 1:
        print(space,"*",space2,"*")
    if star == 1:
        print(space,"*")
for j in range(rows - 1, 0, -1):
    if j > 1:
        star = 2
    elif j == 1:
        star = 1
    space = " " * (rows - j)
    list1.append(rows - j)
    space2 = " " * (((2 * rows) - 1) - (2 * (rows - j) + star))
    list1.append(((2 * rows) - 1) - (2 * (rows - j) + star))
    if star > 1:
        print(space,"*",space2,"*")
    if star == 1:
        print(space,"*")
print(list1)






