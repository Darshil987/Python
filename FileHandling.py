import os

a = input("Enter File name:")
if os.path.exists(a):
    b = input("File Found. Do you want to read or write or delete:")

    if b == 'read' or b == 'Read':
        f = open(a, 'rt')
        print(f.read())
        f.close()

    elif b == 'write' or b == 'Write':
        c = input("Do you want to append or write/replace (a or w):")
        if c == 'a' or c == 'A':
            d = input("Enter Detail you want to append:")
            f = open(a, 'a')
            if f.write(d):
                print("Append successfully.")
            f.close()
        elif c == 'w' or c == 'W':
            d = input("Enter Detail you want to write:")
            f = open(a, 'w')
            if f.write(d):
                print("Write successfully.")
            f.close()
        else:
            print("Please enter 'a' or 'w' only")
    elif b == 'delete' or b == 'Delete':
        try:
            os.remove(a)
            print("Delete Successfully")
        except FileNotFoundError:
            print('Failed! File is not Found')

    else:
        print("Please enter 'read' or 'write' or 'delete' in lower case letter or CamelCase. ")
else:
    print("File not Found :(")
    x = input("Do you want to Create(Y or N):")
    if x == 'Y' or x == 'y':
        a = input("Enter file name:")
        try:
            f = open(a, 'x')
            print('File Created')
            y = input("Do you want to add content(Y or N):")
            if y == 'y' or y == 'Y':
                z = input("Enter Detail you want to write on file:")
                f = open(a, 'w')
                if f.write(z):
                    print("Write successfully.")
                f.close()
            else:
                print("Ok! Come back if you want to add later :) ")
        except FileExistsError:
            print("File already exists")
    else:
        print("Thank you! Have a nice day")
