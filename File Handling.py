import os

try:
    a = input("Enter File Name:")
    f = open(a, 'rt')
    if f.read:
        b = input("File Found.Do you want to read or write or delete:")
        if b == 'read' or b == 'Read':
            print(f.read())
        elif b == 'write' or b == 'write':
            c = input("Do you want to append or write(replace) content (A or W):")
            if c == 'a' or c == 'A':
                d = input("Enter File Content you want to append:")
                f = open(a, 'a')
                if f.write(d):
                    print("Append to file successfully")
                else:
                    print("Error. Please try again.")
            elif c == 'w' or c == 'W':
                d = input("Enter File Content you want to write:")
                f = open(a, 'w')
                if f.write(d):
                    print("Write to file successfully")
                else:
                    print("Error. Please try again.")
            else:
                print("Please enter UPPERCASE/lowercase (A or W) only")
        elif b == 'delete' or b == 'Delete':
            f.close()
            if os.path.exists(a):
                if os.remove(a):
                    print("Sucessfully Deleted")
                else:
                    print("Error")
            else:
                print("Something went wrong. Try again")
        else:
            print("Please enter CamelCase/lowercase (Read/read or Write/write)")
    f.close()

except FileNotFoundError:
    print("Not Found")
    a = input("Do you want to create File (Y or N):")
    if a == 'y' or a == 'Y':
        b = input("Enter File Name:")
        try:
            f = open(b, 'x')
            print("File Created")
            c = input("Do you want to add content (Y or N):")
            if c == 'Y' or c == 'y':
                z = input("Enter Content:")
                f = open(b, 'w')
                if f.write(z):
                    print("Write Successfully")
            f.close()
        except FileExistsError:
            print("File already exists")
    elif a == 'N' or a == 'n':
        print("Thank You, Have a nice day.")
    else:
        print("Please enter Uppercase/lowercase (Y or N)")
