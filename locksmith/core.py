import secrets
import string
from cryptography.fernet import Fernet

def generate_password(length=15):
    """Generate a strong random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def encrypt_password(password, key):
    """Encrypt the password using the provided key."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password, key):
    """Decrypt the password using the provided key."""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password)
    return decrypted.decode()

def save_to_file(filepath, content, binary=True):
    """Save content to a file (binary or text)."""
    mode = 'wb' if binary else 'w'
    with open(filepath, mode) as file:
        file.write(content)

def load_from_file(filepath, binary=True):
    """Load content from a file (binary or text)."""
    mode = 'rb' if binary else 'r'
    with open(filepath, mode) as file:
        content = file.read()
    return content
