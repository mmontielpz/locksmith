import os
import argparse
from locksmith.core import generate_password, generate_key, encrypt_password, save_to_file

# Config
PASSWORDS_DIR = "passwords"
KEYS_DIR = "keys"

# Ensure directories exist
os.makedirs(PASSWORDS_DIR, exist_ok=True)
os.makedirs(KEYS_DIR, exist_ok=True)

def generate_and_save_password(account_name):
    """Generate, encrypt, and save password and key for the given account."""
    # Generate password
    password = generate_password(20)  # Stronger for important accounts
    print(f"Generated password: {password}")

    # Generate key
    key = generate_key()

    # Encrypt password
    encrypted_password = encrypt_password(password, key)

    # Save encrypted password and key
    save_to_file(os.path.join(PASSWORDS_DIR, f"{account_name}.enc"), encrypted_password)
    save_to_file(os.path.join(KEYS_DIR, f"{account_name}.key"), key)

    print(f"🔒 Password encrypted and saved for account: {account_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save an encrypted password for a specific account.")
    parser.add_argument("--account", required=True, help="Account name to associate with the generated password (e.g., work_email_account)")
    args = parser.parse_args()

    generate_and_save_password(args.account)
