try:
    a = input("Enter File Name:")
    f = open(a, 'rt')
    if f.read:
        print("File Found")

except FileNotFoundError:
    print("Not Found")
