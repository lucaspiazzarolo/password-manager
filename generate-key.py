from cryptography.fernet import Fernet

#Function that will generate the encryption key that will be used in your safe!

# Generating the cryptography key and writing it to a file
key = Fernet.generate_key()
with open("pass.key", "wb") as key_file:
    key_file.write(key)
