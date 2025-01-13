#main.py
#imports
import components
import maskpass


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

components.Dashboard()

