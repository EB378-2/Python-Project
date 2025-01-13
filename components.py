import maskpass

def Dashboard(user):
    while True:
        user = user
        x = input(("What would you like to do?\n (1) Change Password\n (2) Change Username\n (3) Add User\n (4) Logout\n"))
        if x == "1":
            change_password(user)
        elif x == "2":
            change_username(user)
        elif x == "3":
            add_user(user)
        else:
            exit()
    


def add_user(user):
    x = 5 

def change_password(user):
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

def change_username(user):
    x = 5