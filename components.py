import maskpass

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
    Passwordfile = open("password.txt", "r")
    print(Passwordfile.read())
    PassChange = input("Would you like to change your password? (y/n)")
    PassChange.lower
    session = 0
    if PassChange == "y" or "":
        for x in range(3):
            session = session + 1
            PasswordAttempt =  maskpass.askpass()
            Passwordfile = open("password.txt", "r")
            PasswordKey = Passwordfile.read()
            print(PasswordKey)
            print(PasswordAttempt)
            if PasswordAttempt == PasswordKey:
                Passwordfile = open("password.txt", "w")
                Passwordfile.write(input("New Password:"))
                break
            else:
                print("Password is wrong! Try again")
                if session == 3:
                    exit()
    else:
        exit()
