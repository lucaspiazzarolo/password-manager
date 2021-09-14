import pyperclip
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
    pyperclip.copy(s_string)

def write_table(u_service, u_login, c_password): #function that stores data in the table
    db, mycursor = connect_database() #connects to database
    mycursor.execute("INSERT INTO PasswordsTable (service, login, password) VALUES (%s, %s, %s)",(u_service, u_login, c_password)) #SQL script to insert new row into table
    db.commit() #commmit changes in table

def check_if_registered(u_service): #function that checks if some string is already present in database
    db, mycursor = connect_database() #connects to database
    
    service_registered = False

    select_query = f"SELECT * FROM PasswordsTable WHERE service = '{u_service}'" #tries to get stored info for this service
    mycursor.execute(select_query)
    if len(mycursor.fetchall()) > 0:
        service_registered = True
    
    return service_registered

def delete_table_row(u_service): #function that deletes one row from table
    service_found = check_if_registered(u_service) #check if this service is already registered in database
    
    if service_found == False:
        print("\n'{}' does not have any register stored in the database. \n".format(u_service))
        print("\n---------- Please select a new option below ----------")
        return None

    db, mycursor = connect_database() #connects to database
    delete_query = f"DELETE FROM PasswordsTable WHERE service = '{u_service}'" #query to delete rows where the service is the one showed
    mycursor.execute(delete_query)
    db.commit()

def change_table_row(u_service): #function that updates one row from table
    service_found = check_if_registered(u_service) #check if this service is already registered in database
    
    if service_found == False:
        print("\n'{}' does not have any register stored in the database. \n".format(u_service))
        print("\n---------- Please select a new option below ----------")
        return None

    db, mycursor = connect_database() #connects to database
    select_query = f"SELECT login, password FROM PasswordsTable WHERE service = '{u_service}'" #retrieves stored password and login for this service
    mycursor.execute(select_query)
    records = mycursor.fetchall()

    for row in records:
        u_login = row[0]
        str_password = decrypt_string(row[1])

    change_login = ""
    change_password = ""

    print("\n---------- Let's update {}'s records! ----------\n".format(u_service))
    while change_login != "y" and change_login != "n":
        try:
            change_login = input("Would you like to change your login info? (y/n): ")
        except ValueError:
            continue
    
    if change_login == "y": #if a new login will be added
            u_login = input("What is your login (or email)? ") #login info

    while change_password != "y" and change_password != "n":
        try:
            change_password = input("Would you like to change your password info? (y/n): ")
        except ValueError:
            continue

    if change_password == "y": #if a new password will be added
        secure_password = ""
        while secure_password != "y" and secure_password != "n":
            try:
                secure_password = input("Would you like to generate a new secure password? (y/n): ")
            except ValueError:
                continue
        if secure_password == "y":
            str_password = generate_password() #calls function to generate the password
        elif secure_password == "n":
            str_password = input("What is your new password? ")

    if change_login == "n" and change_password == "n":
        print("\n---------- Nothing to be updated! ----------")
        return None        
    
    u_password = encrypt_string(str_password) #encrypts password

    copy_to_clipboard(str_password) #copies password to clipboard
    
    delete_table_row(u_service) #deletes outdated row in table
    write_table(u_service, u_login, u_password) #writes new row with updated password
    db.commit() #commits changes into DB
    print("\n---------- {} register successfully updated! Password copied to clipboard! ----------\n".format(u_service))

def show_password(u_service): #function that returns one password from the table
    db, mycursor = connect_database() #connects to database
    select_query = f"SELECT login, password FROM PasswordsTable WHERE service = '{u_service}'" #retrieves all stored passwords for this service
    mycursor.execute(select_query)
    records = mycursor.fetchall()
    for row in records:
        print("\nLogin: ", row[0], end = " ")
        print(" ||  Password: ", decrypt_string(row[1]))
        copy_to_clipboard(decrypt_string(row[1]))
    print("\n---------- Done! Password also copied to clipboard ----------")


def show_logins(): #function that shows all logins stored in the table
    db, mycursor = connect_database() #connects to database
    mycursor.execute("SELECT service, login FROM PasswordsTable ORDER BY service") #Selects all services and logins from Table
    rows = mycursor.fetchall() #gets all rows from selected table
    print("Total records found in database: {}".format(len(rows))) #how many rows in table
    
    for x in rows: #prints each row from table
        print("Service:", end = " ")
        print(*x, sep = " || Login: ")
    
    print("\n---------- Done! ----------")