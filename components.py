import maskpass
import os


def Dashboard(user):
    """
    User Dashboard from where the user can complete 1 of 4 actions.
    """
    while True:
        user = user
        x = input(("What would you like to do?\n (1) Change Password\n (2) Change Username\n (3) Add User\n (4) Logout\n"))
        if x == "1":
            change_password(user)
        elif x == "2":
            change_username(user)
        elif x == "3":
            add_user()
        else:
            exit()
    

def change_password(user):
    """
    A function to allow users to change the password assosiated with their account.
    """
    Passwordfile = open(user, "r")
    PassChange = input("Would you like to change your password? (y/n)")
    PassChange.lower
    session = 0
    if PassChange == "y" or "":
        for x in range(3):
            session = session + 1
            PasswordAttempt =  maskpass.askpass()
            Passwordfile = open(user, "r")
            PasswordKey = Passwordfile.read()
            if PasswordAttempt == PasswordKey:
                Passwordfile = open(user, "w")
                Passwordfile.write(input("New Password:"))
                break
            else:
                print("Password is wrong! Try again")
                if session == 3:
                    exit()
    else:
        exit()

def add_user():
    """
    A function for users to add more users
    """
    new_user = input("New User Username:")
    while True:
        new_user_password = input("Make a password:")
        new_user_password_check = input("Confirm password:")
        if new_user_password == new_user_password_check:
            print("Great, New user set")
            new_user_file = f"{new_user}.txt"
            new_user_file_opened = open(new_user_file, "w")
            new_user_file_opened.write(new_user_password)
            break
        else:
            print("Error: Password does not match. Try again.")


def change_username(user):
    """
    A function to allow users to change their usenames.
    """
    userlog = open(user, "r")
    password = userlog.readline()
    PasswordAttempt =  maskpass.askpass()
    if PasswordAttempt == password:
        new_Username = input("Enter new username:")
        os.remove(user)
        new_user_file = f"{new_Username}.txt"
        new_user_file_opened = open(new_user_file, "w")
        new_user_file_opened.write(password)
        print("Username changed, Logging out...")
        exit()
    else:
        print("Password is wrong!")
