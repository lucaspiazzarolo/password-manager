import logging
import string
import secrets
from cryptography.fernet import Fernet
import mysql.connector
from mysql.connector.errors import InterfaceError

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
    return str(encrypted_password)[2:-1]

def decrypt_string(s_string): #function that decrypts given string
    key = call_key()
    byte_string = s_string.encode()
    decrypted_password = Fernet(key).decrypt(byte_string)
    return str(decrypted_password)[2:-1]

def create_database(): #function that creates "passwords" database
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root", #this password may be different, depending on your MySQL installation
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS passwords") #creates the "passwords" database

def connect_database(): #function that connects to "passwords" database

    create_database() #creates the database, if it does not already exist

    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        database = "passwords"
    )
    mycursor = db.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS PasswordsTable (service VARCHAR(50), login VARCHAR(200), password VARCHAR(200))") #creates the table of stored passwords in the DB, if it does not already exist
    return(db, mycursor)

def copy_to_clipboard(s_string): #function that copies given string to the clipboard
    print(s_string)
    #criar o código

def write_table(u_service, u_login, c_password): #function that stores data in the table
    db, mycursor = connect_database() #connects to database
    #check if service already present into table
    mycursor.execute("INSERT INTO PasswordsTable (service, login, password) VALUES (%s, %s, %s)",(u_service, u_login, c_password)) #SQL script to insert new row into table
    db.commit() #commmit changes in table
    print("\n---------- Password successfully inserted into table! ----------")

def delete_table_row(): #function that deletes one row from table
    print("Hello")
    #criar o código

def show_password(u_service): #function that returns one password from the table
    db, mycursor = connect_database() #connects to database
    select_query = f"SELECT login, password FROM PasswordsTable WHERE service = '{u_service}'" #retrieves all stored passwords for this service
    mycursor.execute(select_query)
    records = mycursor.fetchall()
    for row in records:
        print("\nLogin: ", row[0], end = " ")
        print(" ||  Password: ", decrypt_string(row[1]))

def show_logins(): #function that shows all logins stored in the table
    db, mycursor = connect_database() #connects to database
    mycursor.execute("SELECT service, login FROM PasswordsTable ORDER BY service") #Selects all services and logins from Table
    rows = mycursor.fetchall() #gets all rows from selected table
    print("Total records found in database: {}".format(len(rows))) #how many rows in table
    
    for x in rows: #prints each row from table
        print("Service:", end = " ")
        print(*x, sep = " || Login: ")
    
    print("\n---------- Done! ----------")