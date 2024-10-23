from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

message = "My name is Ashlesha!"
encrypted_message = cipher_suite.encrypt(message.encode())
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

print("Original:", message)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
