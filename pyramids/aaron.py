#xx
def pyramid_1(leng):
    for i in range(leng):
        string = ""
        for j in range(leng-i):
            if j == 0:
                string += "*"
            else:
                string += " *"
        print(string)

def pyramid_2(leng):
    for i in range(leng):
        string = ""
        left_space = leng-i-1
        total_length = leng + i

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            string += "* "

        print(string)

def pyramid_3(leng):
    for i in range(leng):
        string = ""
        left_space = leng- i - 1
        total_length = leng + i + 1

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            string += "* "

        print(string)

def pyramid_4(leng):
    for i in range(leng):
        string = ""
        left_space = leng-i-1
        total_length = leng + i

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            string += "* "

        print(string)

    for i in range(leng-1):
        string = ""
        left_space = i + 1
        total_length = (leng-1) * 2 - i

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            string += "* "

        print(string)

def pyramid_5(leng):
    for i in range(leng):
        string = ""
        left_space = leng-i-1
        total_length = leng + i

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            if j == 0: string += "* "
            elif j == total_length - left_space-1: string += "*"
            else: string += "  "

        print(string)

    for i in range(leng-1):
        string = ""
        left_space = i + 1
        total_length = (leng-1) * 2 - i

        for j in range(left_space):
            string += "  "
        for j in range(total_length - left_space):
            if j == 0: string += "* "
            elif j == total_length - left_space-1: string += "*"
            else: string += "  "

        print(string)

if __name__=="__main__":
    pyramid_1(5)
    pyramid_2(5)
    pyramid_3(5)
    pyramid_4(5)
    pyramid_5(5)