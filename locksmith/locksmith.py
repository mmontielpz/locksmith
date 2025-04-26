import secrets
import string
from cryptography.fernet import Fernet

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password)
    return decrypted.decode()

if __name__ == "__main__":
    # 1. Generate password
    password = generate_password()
    print(f"Generated password: {password}")

    # 2. Generate encryption key
    key = generate_key()

    # 3. Encrypt the password
    encrypted_password = encrypt_password(password, key)
    print(f"Encrypted password: {encrypted_password}")

    # 4. Decrypt the password
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Decrypted password: {decrypted_password}")
