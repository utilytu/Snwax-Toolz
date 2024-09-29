# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.
import hashlib
from cryptography.fernet import Fernet
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
def generate_key():
    return Fernet.generate_key()
def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password
def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password
def main():
    print("Choose an option:")
    print("1. Hash a password")
    print("2. Encrypt/Decrypt a password")
    choice = input("Enter the option (1/2): ")
    if choice == "1":
        password = input("Enter the password to hash: ")
        hashed_password = hash_password(password)
        print(f"Hashed password: {hashed_password}")
    elif choice == "2":
        print("Choose an action:")
        print("1. Encrypt a password")
        print("2. Decrypt a password")
        action = input("Enter the action (1/2): ")
        if action == "1":
            key = generate_key()
            print(f"Encryption key: {key.decode()}")
            password = input("Enter the password to encrypt: ")
            encrypted_password = encrypt_password(password, key)
            print(f"Encrypted password: {encrypted_password.decode()}")
        elif action == "2":
            key = input("Enter the encryption key: ").encode()
            encrypted_password = input("Enter the encrypted password: ").encode()
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"Decrypted password: {decrypted_password}")
        else:
            print("Invalid action selected.")
    else:
        print("Invalid option selected.")
if __name__ == "__main__":
    main()
# Copyright (c) tool IKO/Swnax
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.