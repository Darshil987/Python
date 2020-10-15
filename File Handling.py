try:
    a = input("Enter File Name:")
    f = open(a, 'rt')
    if f.read:
        b = input("File Found.Do you want to read (Y or N):")
        if b == 'y' or b == 'Y':
            print(f.read())
        else:
            print("Ok Bye, Have a nice day")
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
        print("Thank You, Have a nice day")
    else:
        print("Please enter Uppercase/lowercase (Y or N)")
