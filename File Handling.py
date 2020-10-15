try:
    a = input("Enter File Name:")
    f = open(a, 'rt')
    if f.read:
        b = input("File Found.Do you want to read (Y or N) :")
        if b == 'y' or b == 'Y':
            print(f.read())
        else:
            print("Ok Bye, Have a nice day")
    f.close()

except FileNotFoundError:
    print("Not Found")
