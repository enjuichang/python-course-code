rows = int(input("Enter numbers of rows:"))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print("")


for i in range(0, rows+1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)

for i in range(2, rows+1):
    spaces = " " * (rows - i)
    stars = "* " * (i +1 - 1)
    print(spaces + stars)

def print_pattern(rows):
    for i in range(rows ):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print("")
    for i in range(rows - 2, -1, -1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print("")

