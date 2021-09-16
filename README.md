# Summary:

This projects works with an SQL Database, in order to securely store your passwords.

How it works: There is a master password used to access your "safe". From that point on, you can manage your passwords (create new secure ones, store existing passwords, view, edit and delete them).

I took a time in order to try and make this as safe as possible (using hash functions, with "salt" and "pepper" for the main password, and cryptography for storing all passwords in the database)

# Libraries needed:

Libraries needed to use everything in this script:
    1. cryptography
    2. mysql
    3. pyperclip

# First Setup:

The first thing you should do is to run the "hash-engine.py" script in order to get your "hashed" secure password. (you may also change your 'salt' in row #5)
After doing that, you get your hashed password and update it in "password-safe.py" row #11
Now you have your own master password working!

After that, you might generate a new "pass.key" file, so you have your own encrypt/decrypt key (not mandatory)

Lastly, if you find some connectivity errors with the MYSQL, please check login and password informations in "functions.py" file, rows 44-46 and rows 56-58.

Hope you all enjoy it! :)