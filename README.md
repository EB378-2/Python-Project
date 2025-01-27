***Documentation***
**Target assessment level**
Target assessment level of this work is 3.

**Specification**
The program
1. Takes user input and processes a log in based on the existance of a profile txt file.
2. Allows the user to modify the details regarding the users own profile, such as username and login password. 
3. Allows users to create new profiles.

The user conduct entire process in the user's termial.

Each profile has 1 respective txt file, named as {username}.txt, containing a password to the log in. 


**Correctness**

*Typical test case*

User has a file under their username. When the program (file main.py) is run the output is correct, with a prompt for a username, then password for the user to fill-in and then have access to modify, add, and play with the program. A log out will result in the end of the program which can be restarted by re running the file. all changes will be saved from the previous session, unless the repository is not saved or the codebase is modified.

> give path to program file: main.py
> Username:
> Enter Password: 
> Welcome Sir
> What would you like to do?
> (1) Change Password
> (2) Change Username
> (3) Add User
> (4) Logout
> 

Simply select the next course of action with the numbers.


**Resource management (level 2)**
The profile file is opened and closed after use.


**External libraies**
- maskpass is used to hid the password input when the user enters the password into his terminal.