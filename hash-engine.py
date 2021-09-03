#Script that makes the hashing, so the user can define his secure (hashed) password
import hashlib

password = input("Please provide your password: ") #password that later should be used in the password safe
salt = "x\¨Ngy7"

hashed_password = hashlib.sha1((password + salt).encode('utf-8')) #hashes the password

print("Your hashed password (with salt) is: {}".format(hashed_password.hexdigest())) #move this hashed password to the 'password-safe.py' code (line 16)
