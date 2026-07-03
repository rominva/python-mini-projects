# << PSSWORD MANAGEMENT >>
# 1) modes: view, add, quit
# 2) add new passwords (in a .txt)
# 3) view password
# 4) encrypt passwords
# 5) decrypt password

from cryptography.fernet import *

# creat a key just for once:
# with open("./mykey_3.key", "wb") as f:
#     key = Fernet.generate_key()
#     f.write(key)


def load_key():
    with open("./mykey_3.key", "rb") as f:
        return f.read()


key = load_key()
encryptor = Fernet(key)


def add_pass(username, password):
    with open("./password_3.txt", "a") as f:
        encrypted_pass = encryptor.encrypt(password.encode()).decode()
        f.write(f"{username} | {encrypted_pass}\n")
    print("password added successfully!\n")


def view_pass():
    with open("./password_3.txt", "r") as file:
        for item in file:
            item = item.rstrip()
            username, encrypted_pass = item.split("|")
            password = encryptor.decrypt(encrypted_pass).decode()
            print(f"USERNAME: {username} | PASSWORD: {password}")


while True:
    user_choice = input("Choose a Mode; v:view, a:add, q:quit\n").lower()

    if user_choice == "v":
        print("your passwords:")
        view_pass()

    elif user_choice == "a":
        print("let's add a new password!")
        username = input("1)Enter a new username: ")
        password = input("2)Enter a new password: ")
        add_pass(username, password)

    elif user_choice == "q":
        break

    else:
        print("Wrong Mode!")
