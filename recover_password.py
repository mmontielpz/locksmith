import argparse
import os
from locksmith.core import decrypt_password, load_from_file

# Config paths
PASSWORDS_DIR = "passwords"
KEYS_DIR = "keys"

def recover_password(account_name):
    """Recover and decrypt the password for a given account."""
    encrypted_password_path = os.path.join(PASSWORDS_DIR, f"{account_name}.enc")
    key_path = os.path.join(KEYS_DIR, f"{account_name}.key")

    if not os.path.exists(encrypted_password_path):
        print(f"❌ Encrypted password file not found: {encrypted_password_path}")
        return

    if not os.path.exists(key_path):
        print(f"❌ Key file not found: {key_path}")
        return

    encrypted_password = load_from_file(encrypted_password_path, binary=True)
    key = load_from_file(key_path, binary=True)

    password = decrypt_password(encrypted_password, key)
    print(f"🔓 Decrypted password for account '{account_name}':\n\n{password}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recover a stored password by account name.")
    parser.add_argument("--account", required=True, help="Account name (e.g., work_email_account)")
    args = parser.parse_args()

    recover_password(args.account)
