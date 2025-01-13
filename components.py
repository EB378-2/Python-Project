import maskpass

def Auth():
    while True:
        UsernameAttempt = input("Username:")
        PasswordAttempt =  maskpass.askpass()
        user = f"{UsernameAttempt}.txt"
        userlog = open(user, "r")
        password = userlog.readline()
        if PasswordAttempt == password:
            print("Welcome Sir")
            break
        else:
            print("Password is wrong!")
            print(password) #Debug

def Dashboard():
    userlog = open("user.txt", "r")
    user = userlog.read()
    Passwordfile = open(user, "r")
    print(Passwordfile.read())
    PassChange = input("Would you like to change your password? (y/n)")
    PassChange.lower
    session = 0
    if PassChange == "y" or "":
        for x in range(3):
            session = session + 1
            PasswordAttempt =  maskpass.askpass()
            Passwordfile = open(user, "r")
            PasswordKey = Passwordfile.read()
            print(PasswordKey)
            print(PasswordAttempt)
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
    x = 5 

def change_password():
    x = 5

def change_username():
    x = 5