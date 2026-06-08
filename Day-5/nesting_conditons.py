# Nesting :- means placing one block of code inside another.

#login system

username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "pass":
    print("login successfully")
else:
    if username != "admin":
        print("wrong username, try again")
    else:
        print("wrong password, try again")        