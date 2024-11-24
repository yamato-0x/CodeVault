import os
import json
from cryptography.fernet import Fernet

# Generate a key and save it to a file (run this once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the file
def load_key():
    with open("key.key", "rb") as key_file:
        return Fernet(key_file.read())

# Add a secret to the vault
def add_secret(name, value):
    f = load_key()
    encrypted_value = f.encrypt(value.encode())
    
    if not os.path.exists("vault.json"):
        with open("vault.json", "w") as file:
            json.dump({}, file)

    with open("vault.json", "r") as file:
        secrets = json.load(file)

    secrets[name] = encrypted_value.decode()

    with open("vault.json", "w") as file:
        json.dump(secrets, file)

# Get a secret from the vault
def get_secret(name):
    f = load_key()
    with open("vault.json", "r") as file:
        secrets = json.load(file)

    if name in secrets:
        return f.decrypt(secrets[name].encode()).decode()
    else:
        return None

# Main menu
def menu():
    print("Welcome to Code Vault!")
    print("1. Add a secret")
    print("2. Get a secret")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter the name of the secret: ")
        value = input("Enter the value of the secret: ")
        add_secret(name, value)
        print(f"Secret '{name}' added!")
    elif choice == "2":
        name = input("Enter the name of the secret: ")
        secret = get_secret(name)
        if secret:
            print(f"Your secret: {secret}")
        else:
            print("Secret not found.")
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice!")

# Run the app
if __name__ == "__main__":
    if not os.path.exists("key.key"):
        generate_key()
    while True:
        menu()
