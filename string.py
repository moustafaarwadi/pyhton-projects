username = input("enter your username: ")

if len(username) > 12:
    print("your username can't be more than 12 character.")
elif not username.find(" ") == -1:
    print("your username can't contain a space.")
elif not username.isalpha():
    print("your username can't contain any digit.")
else:
    print(f"welcome {username}")