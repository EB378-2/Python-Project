from tkinter import Y
import maskpass
from sympy import Range

def Auth():
    Passwordfile= open("password.txt")
    PasswordKey = Passwordfile.read()
    while True:
        PasswordAttempt =  maskpass.askpass()
        if PasswordAttempt == PasswordKey:
            print("Welcome Sir")
            break
        else:
            print("Password is wrong!")

def Dashboard():
    Passwordfile= open("password.txt")
    Passwordfile1= open("password.txt", "w")
    Name = input("What is your name?")
    PassChange = input("Would you like to change your password? (y/n)")
    PassChange.lower
    session = 0
    if PassChange == "y" or "":
        for x in Range(3):
            session = session + 1
            PasswordAttempt =  maskpass.askpass()
            PasswordKey = Passwordfile.read()
            if PasswordAttempt == PasswordKey:
                Passwordfile1.write(input("New Password:"))
                break
            else:
                print("Password is wrong! Try again")
                if session == 3:
                    exit()
