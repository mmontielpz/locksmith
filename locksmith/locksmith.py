import os
from locksmith.core import generate_password, generate_key, encrypt_password, decrypt_password, save_to_file, load_from_file

# Config
account_name = "itj"
passwords_dir = "passwords"
keys_dir = "keys"

# Ensure directories exist
os.makedirs(passwords_dir, exist_ok=True)
os.makedirs(keys_dir, exist_ok=True)

if __name__ == "__main__":
    # Generate password
    password = generate_password(20)  # stronger for work accounts
    print(f"Generated password: {password}")

    # Generate key
    key = generate_key()

    # Encrypt password
    encrypted_password = encrypt_password(password, key)

    # Save encrypted password and key
    save_to_file(f"{passwords_dir}/{account_name}.enc", encrypted_password)
    save_to_file(f"{keys_dir}/{account_name}.key", key)

    print(f"🔒 Password encrypted and saved for account: {account_name}")
