#must be 12 letters long
#must not contain spaces
#myst not contain numbers

username = input("Username: ")

if len(username) > 12:
	print("Username must be at most 12 characters long.")
elif " " in username:
    print ("your username MUST not contain spaces")
elif not username.isalpha():
    print ("your username MUST not contain NUMBERS")
else:
    print (f"welcome {username}")   