# password-manager

Libraries needed to use everything in this script:
    1. cryptography
    2. mysql
    3. pyperclip

This projects creates a password safe in a local SQL database, and helps you store secure passwords.

The first thing you should do is to run the "hash-engine.py" script in order to get your "hashed" secure password. (you may also change your 'salt' in row #5)
After doing that, you get your hashed password and update it in "password-safe.py" row #11
Now you have your own master password working!

After that, you might generate a new "pass.key" file, so you have your own encrypt/decrypt key (not mandatory)

Lastly, if you find some connectivity errors with the MYSQL, please check login and password informations in "functions.py" file, rows 44-46 and rows 56-58.

Hope you all enjoy it! :)