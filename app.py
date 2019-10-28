import os


def createPassword():
    passwordready = False
    while passwordready == False:
        password = input("Create your password: ")
        confirm_password = input("Confirm password: ")
        passwordready = password == confirm_password
        if passwordready == False:
            print("Password didn't match")

    return password

def PasswordExist():
    return True

def Credential():
    if PasswordExist() == True:
        return input("input password: ")
    else:
        return createPassword()


password = Credential()

print("\n\nPress any key below to create or open folder\n"
"c. Create Folder\n"
"1. folder1\n"
"2. folder2")

key = input("Input key: ")

if key == 'c':
    input ("Folder name: ")


