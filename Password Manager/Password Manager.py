MasterPassword = input("What is the master password?")


def view():
     with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

def add():
    name = input("Account Name:")
    password = input("Password:")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    choice = input("Would you like to add a new password or view exisiting ones (view, add)?, press q to quit.")

    if choice == "q":
        break

    if choice == "view":
        view()
    elif choice == "add":
        add()
    else:
     print("invalid choice.")
     continue
