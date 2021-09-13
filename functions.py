import string
import secrets
from cryptography.fernet import Fernet
import mysql.connector

def generate_password(): #function that generate a password, based on some user inputs
    num_chars = 0
    special_chars = ""

    while not(num_chars > 0 and num_chars <= 30):
        try:
            num_chars = int(input("How many characters will your password have? (1 - 30): ")) #user defines how many characters his/her password will have
        except ValueError:
                continue

    while (special_chars != "y" and special_chars != "n"):
        special_chars = input("Would you like your password to have special chars? (y/n): ") #user chooses if there will be special characters in the password
    
    if special_chars == "y":
        return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num_chars)) #returns password
    elif special_chars == "n":
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num_chars)) #returns password

# Function to load encryption key
def call_key():
    return open("pass.key", "rb").read()

def encrypt_string(s_string): #function that encrypts given string
    key = call_key()
    regular_password = s_string.encode()
    encrypted_password = Fernet(key).encrypt(regular_password)
    print(str(encrypted_password))
    return str(encrypted_password)[2:-1]

def decrypt_string(s_string): #function that decrypts given string
    key = call_key()
    byte_string = s_string.encode()
    decrypted_password = Fernet(key).decrypt(byte_string)
    print(str(decrypted_password))
    return str(decrypted_password)[2:-1]

def connect_database(): #function that connects to "passwords" database
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        database = "passwords"
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE StoredPassword (service VARCHAR(50), login VARCHAR(50), password VARCHAR(50))")


def copy_to_clipboard(s_string): #function that copies given string to the clipboard
    print(s_string)
    #criar o código

def create_table(): #function that creates the table to store the passwords
    print("Hello")
    #criar o código

def write_table(): #function that stores data in the table
    print("Hello")
    #criar o código

def delete_table_row(): #function that deletes one row from table
    print("Hello")
    #criar o código

def show_password(): #function that returns one password from the table
    print("Hello")
    #criar o código

def show_logins(): #function that shows all logins stored in the table
    print("Hello")
    #criar o código 