from locksmith.core import generate_password, generate_key, encrypt_password, decrypt_password

def manual_tests():
    print("Running Locksmith Core Manual Tests...")

    # 1. Password Generation
    password = generate_password()
    print(f"Generated password: {password}")
    assert len(password) == 15, "Password should be 15 characters long"
    print("[PASS] Password Generation")

    # 2. Key Generation
    key = generate_key()
    print(f"Generated key: {key}")
    assert len(key) == 44, "Fernet key should be 44 characters (base64-encoded 32 bytes)"
    print("[PASS] Key Generation")

    # 3. Encryption
    encrypted_password = encrypt_password(password, key)
    print(f"Encrypted password: {encrypted_password}")
    assert isinstance(encrypted_password, bytes), "Encrypted password should be bytes"
    print("[PASS] Password Encryption")

    # 4. Decryption
    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Decrypted password: {decrypted_password}")
    assert decrypted_password == password, "Decrypted password should match original"
    print("[PASS] Password Decryption")

    print("✅ All Manual Tests Passed!")

if __name__ == "__main__":
    manual_tests()
