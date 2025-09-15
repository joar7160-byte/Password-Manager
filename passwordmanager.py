import getpass
import bcrypt

password_manager = {}

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:

    return bcrypt.checkpw(password.encode(), hashed)

def create_account():
    username = input("Username: ").strip()
    if username in password_manager:
        print("Username already exists")
        return
    
    password = getpass.getpass("Password: ")
    hashed_password = hash_password(password)
    password_manager[username] = hashed_password
    print("Account Created")

def login():
    username = input("Enter your username: ").strip()
    if username not in password_manager:
        print("Invalid username")
        return
    
    password = getpass.getpass("Enter your password: ")
    hashed_password = password_manager[username]

    if verify_password(password, hashed_password):
        print("Login successful!")
    else:
        print("Invalid password")

def main():
    while True:
        choice = input("\nEnter 1 to create an account, 2 to login, or 0 to exit: ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()